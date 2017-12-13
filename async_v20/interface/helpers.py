from functools import partial
from inspect import _empty

from ..definitions.base import create_attribute
from ..definitions.types import OrderRequest


def _in_context(order_request, instrument, clip=False):
    """Ensure the order request is formatted as per the instrument specification
    """

    formatted_attributes = {}

    if clip:
        formatted_attributes.update(
            units=order_request.units.format(
                instrument.trade_units_precision,
                instrument.minimum_trade_size,
                instrument.maximum_order_units))
    elif instrument.minimum_trade_size < order_request.units < \
            instrument.maximum_order_units:
        formatted_attributes.update(
            units=order_request.units.format(
                instrument.trade_units_precision))
    else:
        raise ValueError(f'OrderRequest units {order_request.units} '
                         f'are less than the minimum trade size {instrument.minimum_trade_size}')

    for attr in ('price', 'price_bound', 'distance'):
        value = getattr(order_request, attr, None)
        if value:
            formatted_attributes.update(
                attr=value.format(instrument.display_precision)
            )

    for attr in ('take_profit_on_fill', 'stop_loss_on_fill'):
        value = getattr(order_request, attr, None)
        if value:
            formatted_attributes.update(
                attr=value.replace(
                    price=value.price.format(instrument.display_precision))
            )

    attr = 'trailing_stop_loss_on_fill'
    value = getattr(order_request, attr, None)
    if value:
        if clip:
            formatted_attributes.update(
                attr=value.replace(
                    distance=value.distance.format(
                        instrument.display_precision,
                        instrument.minimum_trailing_stop_distance,
                        instrument.maximum_trailing_stop_distance)))

        elif instrument.minimum_trailing_stop_distance < value.distance < \
                instrument.maximum_trailing_stop_distance:
            formatted_attributes.update(
                attr=value.replace(
                    distance=value.distance.format(
                        instrument.display_precision)))
        else:
            raise ValueError(f'Trailing stop loss distance is not '
                             f'{instrument.minimum_trailing_stop_distance} < {value.distance} < '
                             f'{instrument.maximum_trailing_stop_distance}')

    return order_request.replace(**formatted_attributes)


def _arguments(endpoint, param_location):
    return ((parameter['name'], parameter['type']) for parameter in endpoint.parameters if
            parameter['located'] == param_location)


def _create_request_params(self, endpoint, arguments: dict, param_location: str):
    possible_arguments = _arguments(endpoint, param_location)

    def lookup():
        for name, typ in possible_arguments:
            try:
                result = arguments[typ]
            except KeyError:
                try:
                    result = self.default_parameters[typ]
                except KeyError:
                    continue

            yield name, result

    return dict(lookup())


def construct_path(template, arguments, default_arguments):
    path = ''
    for segment in template:
        try:
            path += segment
        except TypeError:  # Need to cast to string as specifier may be an int.
            # Means segment wasn't a string
            try:
                path += str(arguments[segment])
            except KeyError:
                # Means the segment wasn't passed in the arguments
                try:
                    path += str(default_arguments[segment])
                except KeyError:
                    # Means path can not be constructed
                    raise ValueError(f'Missing {segment} in arguments in supplied arguments {arguments}')
    return path


def create_url(self, endpoint, arguments):
    try:
        path = construct_path(endpoint.path, arguments, self.default_parameters)
    except ValueError:
        raise ValueError(f'Unable to construct path for {endpoint}')

    host = self.hosts[endpoint.host]
    return host(path=path)


def create_body(self, request_schema, arguments):
    """Create the JSON body to add to the HTTP request

    Args:
        request_schema: -- the endpoints request schema
        arguments: -- dict of user supplied arguments

    Returns:
        Dict containing the formatted data
    """

    # Reverse the request schema to allow for lookups

    def dumps():
        """Iterate over the arguments returning dicts of matching objects
        and format order requests where required"""
        for key, value in arguments.items():
            try:
                key = request_schema[key]
            except KeyError:
                continue
            else:
                if isinstance(value, OrderRequest):
                    value = _in_context(value,
                                        self._instruments.get_instrument(value.instrument),
                                        self.format_order_requests)
                try:
                    value = value.dict(json=True)
                except AttributeError:
                    pass
                yield key, value

    return dict(tuple(dumps()))


header_params = partial(_create_request_params, param_location='header')

query_params = partial(_create_request_params, param_location='query')


def construct_arguments(signature, bound_arguments):
    """Construct passed arguments into corresponding objects

    args:

        signature: -- Signature of api method
        bound_arguments:

    Returns:
        dict with annotation with as keys and annotation instances as values
        """

    def yield_annotations():
        for name, value in bound_arguments.items():
            annotation = signature.parameters[name].annotation
            if not annotation == _empty and not value == ...:
                yield annotation, create_attribute(annotation, value)

    return dict(yield_annotations())


def create_request_kwargs(self, endpoint, sig, *args, **kwargs):
    """Format arguments to be passed to an aiohttp request"""
    bound = sig.bind(self, *args, **kwargs)
    bound.apply_defaults()
    arguments = construct_arguments(sig, bound.arguments)

    json = create_body(self, endpoint.request_schema, arguments)

    headers = header_params(self, endpoint, arguments)
    url = create_url(self, endpoint, arguments)

    # yarl doesn't accept int subclass'
    parameters = {k: str(v) for k, v in query_params(self, endpoint, arguments).items()}

    request_kwargs = {
        'method': endpoint.method,
        'url': url,
        'headers': headers,
        'params': parameters,
        'json': json,
    }

    if endpoint.host == 'STREAM':
        request_kwargs.update({'timeout': 0})

    return request_kwargs
