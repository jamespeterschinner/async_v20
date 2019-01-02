import logging
from functools import partial
from inspect import _empty

import pandas as pd

from ..definitions.base import create_attribute
from ..definitions.types import OrderRequest
from ..definitions.helpers import sentinel
from ..endpoints.annotations import LastTransactionID
from ..endpoints.annotations import SinceTransactionID
from ..exceptions import FailedToCreatePath, InvalidOrderRequest

logger = logging.getLogger(__name__)

STOP = 'STOP'
MARKET = 'MARKET'
MARKET_IF_TOUCHED = 'MARKET_IF_TOUCHED'
LIMIT = 'LIMIT'
INSTRUMENT = 'instrument'
UNITS = 'units'
ALLOWED_SINCE_TRANSACTION_ID = 900


def _format_order_request(order_request, instrument, clip=False):
    """Ensure the order request is formatted as per the instrument specification
    """

    formatted_attributes = {}
    if hasattr(order_request, UNITS):

        if clip:
            formatted_attributes.update(
                units=order_request.units.format(
                    instrument.trade_units_precision,
                    instrument.minimum_trade_size,
                    instrument.maximum_order_units))
        elif instrument.minimum_trade_size <= abs(order_request.units) <= \
                instrument.maximum_order_units:
            formatted_attributes.update(
                units=order_request.units.format(
                    instrument.trade_units_precision))
        else:
            msg = f'OrderRequest units {order_request.units} {instrument.name} specified range ' \
                  f'{instrument.minimum_trade_size} - {instrument.maximum_order_units}'
            logger.error(msg)
            raise InvalidOrderRequest(msg)

    for attr in ('price', 'price_bound', 'distance'):
        value = getattr(order_request, attr, None)
        if value:
            formatted_attributes.update(
                {attr: value.format(instrument.display_precision)}
            )

    for attr in ('take_profit_on_fill', 'stop_loss_on_fill'):
        value = getattr(order_request, attr, None)
        if value:
            formatted_attributes.update(
                {attr: value.replace(price=value.price.format(instrument.display_precision))}
            )

    attr = 'trailing_stop_loss_on_fill'
    value = getattr(order_request, attr, None)
    if value:
        if clip:
            formatted_attributes.update(
                {attr: value.replace(
                    distance=value.distance.format(
                        instrument.display_precision,
                        instrument.minimum_trailing_stop_distance,
                        instrument.maximum_trailing_stop_distance))}
            )

        elif instrument.minimum_trailing_stop_distance <= value.distance <= \
                instrument.maximum_trailing_stop_distance:
            formatted_attributes.update(
                {attr: value.replace(
                    distance=value.distance.format(
                        instrument.display_precision))}
            )
        else:
            msg = f'Trailing stop loss distance {value.distance} is not within {instrument.name} ' \
                  f'specified range {instrument.minimum_trailing_stop_distance} - ' \
                  f'{instrument.maximum_trailing_stop_distance}'
            logger.error(msg)
            raise InvalidOrderRequest(msg)
    return order_request.replace(**formatted_attributes)


def _create_request_params(self, endpoint, arguments: dict, param_location: str):
    def lookup():
        for typ, (location, name) in endpoint.parameters.items():
            if not location == param_location:
                # Skip parameters if they are not in the desired location
                continue
            try:
                result = arguments[typ]
            except KeyError:
                try:
                    result = self.default_parameters[typ]
                except KeyError:
                    continue

            if isinstance(result, pd.Timestamp):
                # json method added in primitives module
                result = result.json(self.datetime_format)
            else:
                result = str(result)

            yield name, str(result)

    return dict(lookup())


def create_url(self, endpoint, arguments):
    path = ''
    for segment in endpoint.path:
        try:
            path += segment
        except TypeError:
            # Segment wasn't a string. Meaning it is a required parameter.
            try:
                # Need to cast to string as specifier may be an int.
                path += str(arguments[segment])
            except KeyError:
                # Means the segment wasn't passed in the arguments
                try:
                    path += str(self.default_parameters[segment])
                except KeyError:
                    # Means path can not be constructed
                    msg = f'Could not construct path for {endpoint.__class__.__name__}. ' \
                          f'{segment} is missing in supplied arguments {arguments}'
                    logger.error(msg)
                    raise FailedToCreatePath(msg)

    host = self._hosts[endpoint.host]
    return host(path=path)


def create_body(self, request_schema, arguments):
    """Create the JSON body to add to the HTTP request

    Args:
        request_schema: -- the endpoints request schema
        arguments: -- dict of user supplied arguments

    Returns:
        Dict containing the formatted data
    """

    def dumps():
        """Iterate over the arguments returning dicts of matching objects
        and format order requests where required"""
        for key, value in arguments.items():
            try:
                key = request_schema[key]
            except KeyError:
                continue
            else:
                # Only attempt to format OrderRequests that have an `instrument` attribute
                if isinstance(value, OrderRequest):
                    instrument = self.instruments.get_instrument(value.instrument)
                    if instrument is not None:
                        value = _format_order_request(value,
                                                      instrument,
                                                      self.format_order_requests)
                    else:
                        msg = f'The instrument specified instrument {value.instrument} ' \
                              f'for OrderRequest {value} is not tradeable by this account'
                        logger.error(msg)
                        raise InvalidOrderRequest(msg)

                try:
                    value = value.dict(json=True, datetime_format=self.datetime_format)
                except AttributeError:
                    pass
                yield key, value

    return dict(tuple(dumps()))


header_params = partial(_create_request_params, param_location='header')

query_params = partial(_create_request_params, param_location='query')


def too_many_passed_transactions(self):
    try:
        if (self.default_parameters[LastTransactionID] -
            self.default_parameters[SinceTransactionID]) > ALLOWED_SINCE_TRANSACTION_ID:
            return True
    except KeyError:
        # Means client isn't initialized
        pass
    return False


def construct_arguments(self, sig, *args, **kwargs):
    """Construct passed arguments into corresponding objects

    args:

        signature: -- Signature of api method
        bound_arguments:

    Returns:
        dict with annotation with as keys and annotation instances as values
        """

    bound = sig.bind(self, *args, **kwargs)
    bound.apply_defaults()

    def yield_annotations():
        for name, value in bound.arguments.items():
            annotation = sig.parameters[name].annotation

            if value == sentinel:
                try:
                    value = self.default_parameters[annotation]
                except KeyError:
                    continue

                if issubclass(annotation, SinceTransactionID) \
                        and too_many_passed_transactions(self):
                    logging.warning('Too many transactions have passed to use the default '
                                    '`since_transaction_id` value.')
                    value = self.default_parameters[LastTransactionID] - ALLOWED_SINCE_TRANSACTION_ID

            if issubclass(annotation, SinceTransactionID) \
                    and too_many_passed_transactions(self):
                logging.warning(f'The passed `since_transaction_id` value {value} '
                                f'is more than {ALLOWED_SINCE_TRANSACTION_ID} transactions ago.')

            if not annotation == _empty:
                yield annotation, create_attribute(annotation, value)

    return dict(yield_annotations())


def create_request_kwargs(self, endpoint, arguments):
    """Format arguments to be passed to an aiohttp request"""

    json = create_body(self, endpoint.request_schema, arguments)

    headers = header_params(self, endpoint, arguments)

    url = create_url(self, endpoint, arguments)

    # yarl doesn't accept int subclass'
    parameters = query_params(self, endpoint, arguments)

    request_kwargs = {}
    for parameter, value in (
            ('method', endpoint.method),
            ('url', url),
            ('headers', headers),
            ('params', parameters),
            ('json', json)):
        if not value:
            continue
        else:
            request_kwargs.update({parameter: value})

    return request_kwargs
