from functools import partial
from inspect import _empty

from async_v20.definitions.types import Account
from async_v20.definitions.types import AccountChanges
from async_v20.definitions.types import AccountChangesState
from async_v20.definitions.types import ArrayTransaction
from ..definitions.base import create_attribute


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


def create_url(self, endpoint, arguments):
    endpoint_path = endpoint.path(arguments, default=self.default_parameters)
    host = self.hosts[endpoint.host]
    return host(path=endpoint_path)


def create_body(request_schema, arguments):
    """Create the JSON body to add to the HTTP request

    Args:
        request_schema: -- the endpoints request schema
        arguments: -- dict of user supplied arguments

    Returns:
        Dict containing the formatted data
    """

    # Reverse the request schema to allow for lookups

    def dumps():
        """Iterate over the arguments returning dicts of matching objects"""
        for key, value in arguments.items():
            try:
                key = request_schema[key]
            except KeyError:
                continue
            else:
                try:
                    value = value.dict()
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
            if not annotation == _empty:
                yield annotation, create_attribute(annotation, value)

    return dict(yield_annotations())


def create_request_kwargs(self, endpoint, sig, *args, **kwargs):
    """Format arguments to be passed to an aiohttp request"""
    arguments = sig.bind(self, *args, **kwargs).arguments
    arguments = construct_arguments(sig, arguments)

    json = create_body(endpoint.request_schema, arguments)

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


def update_account(self, changes: AccountChanges, changes_state: AccountChangesState) -> (Account, ArrayTransaction):
    """Update an existing account with changes

    Args:
        account: -- The account instance to update
        transactions: -- An iterable of Transactions to append to
        changes: -- Changes from account_changes API call
        changes_state: ChangesState from account_changes API call

    Returns:
        (Account, ArrayTransaction)

    """

    # remove, replace, add changed orders
    orders = list(changes.orders_created)
    for order in self._account.orders:
        if not changes.orders_cancelled.get_id(order.id) \
                and not changes.orders_filled.get_id(order.id):
            # Don't add an existing order to the new account instance
            # if it has been cancelled or filled
            triggered_order = changes.orders_triggered.get_id(order.id)
            if triggered_order:
                order = triggered_order
            orders.append(order)

    # All new open trades need to be added to account
    trades = list(changes.trades_opened)
    for trade in self._account.trades:
        if not changes.trades_closed.get_id(trade.id):
            # Replace the trade if it has been reduced
            reduced_trade = changes.trades_reduced.get_id(trade.id)
            if reduced_trade:
                trade = reduced_trade

            trades.append(trade)

    # get_account_details does not provide transaction history
    # Account specification has no transactions
    transactions = ArrayTransaction(*[*self.transactions, *changes.transactions])

    updated_account = self._account.replace(
        orders=orders,
        trades=trades,
        positions=changes.positions,
        unrealized_pl=changes_state.unrealized_pl,
        nav=changes_state.nav,
        margin_used=changes_state.margin_used,
        margin_available=changes_state.margin_available,
        position_value=changes_state.position_value,
        margin_closeout_unrealized_pl=changes_state.margin_closeout_unrealized_pl,
        margin_closeout_nav=changes_state.margin_closeout_nav,
        margin_closeout_margin_used=changes_state.margin_closeout_margin_used,
        margin_closeout_percent=changes_state.margin_closeout_percent,
        margin_closeout_position_value=changes_state.margin_closeout_position_value,
        withdrawal_limit=changes_state.withdrawal_limit,
        margin_call_margin_used=changes_state.margin_call_margin_used,
        margin_call_percent=changes_state.margin_call_percent
    )
    return updated_account, transactions
