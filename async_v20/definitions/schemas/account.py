from ..types import *
from ...endpoints.metaclass import Array

default = lambda x: x
required = True
boolean = bool
integer = int
string = str

class Accountobject:
    """The full details of a client’s Account. This includes
    full open Trade, open Position and pending Order representation.
    """
    # JSON representation of object
    schema = {
        # The Account’s identifier
        'id': AccountID,
        # Client-assigned alias for the Account. Only provided if the Account has
        # an alias set
        'alias': string,
        # The home currency of the Account
        'currency': Currency,
        # The current balance of the Account. Represented in the Account’s home
        # currency.
        'balance': AccountUnits,
        # ID of the user that created the Account.
        'createdByUserID': integer,
        # The date/time when the Account was created.
        'createdTime': DateTime,
        # The total profit/loss realized over the lifetime of the Account.
        # Represented in the Account’s home currency.
        'pl': AccountUnits,
        # The total realized profit/loss for the Account since it was last reset by
        # the client. Represented in the Account’s home currency.
        'resettablePL': AccountUnits,
        # The date/time that the Account’s resettablePL was last reset.
        'resettabledPLTime': DateTime,
        # The total amount of commission paid over the lifetime of the Account.
        # Represented in the Account’s home currency.
        'commission': AccountUnits,
        # Client-provided margin rate override for the Account. The effective
        # margin rate of the Account is the lesser of this value and the OANDA
        # margin rate for the Account’s division. This value is only provided if a
        # margin rate override exists for the Account.
        'marginRate': DecimalNumber,
        # The date/time when the Account entered a margin call state. Only provided
        # if the Account is in a margin call.
        'marginCallEnterTime': DateTime,
        # The number of times that the Account’s current margin call was extended.
        'marginCallExtensionCount': integer,
        # The date/time of the Account’s last margin call extension.
        'lastMarginCallExtensionTime': DateTime,
        # The number of Trades currently open in the Account.
        'openTradeCount': integer,
        # The number of Positions currently open in the Account.
        'openPositionCount': integer,
        # The number of Orders currently pending in the Account.
        'pendingOrderCount': integer,
        # Flag indicating that the Account has hedging enabled.
        'hedgingEnabled': boolean,
        # The total unrealized profit/loss for all Trades currently open in the
        # Account. Represented in the Account’s home currency.
        'unrealizedPL': AccountUnits,
        # The net asset value of the Account. Equal to Account balance +
        # unrealizedPL. Represented in the Account’s home currency.
        'NAV': AccountUnits,
        # Margin currently used for the Account. Represented in the Account’s home
        # currency.
        'marginUsed': AccountUnits,
        # Margin available for Account. Represented in the Account’s home currency.
        'marginAvailable': AccountUnits,
        # The value of the Account’s open positions represented in the Account’s
        # home currency.
        'positionValue': AccountUnits,
        # The Account’s margin closeout unrealized PL.
        'marginCloseoutUnrealizedPL': AccountUnits,
        # The Account’s margin closeout NAV.
        'marginCloseoutNAV': AccountUnits,
        # The Account’s margin closeout margin used.
        'marginCloseoutMarginUsed': AccountUnits,
        # The Account’s margin closeout percentage. When this value is 1.0 or above
        # the Account is in a margin closeout situation.
        'marginCloseoutPercent': DecimalNumber,
        # The value of the Account’s open positions as used for margin closeout
        # calculations represented in the Account’s home currency.
        'marginCloseoutPositionValue': DecimalNumber,
        # The current WithdrawalLimit for the account which will be zero or a
        # positive value indicating how much can be withdrawn from the account.
        'withdrawalLimit': AccountUnits,
        # The Account’s margin call margin used.
        'marginCallMarginUsed': AccountUnits,
        # The Account’s margin call percentage. When this value is 1.0 or above the
        # Account is in a margin call situation.
        'marginCallPercent': DecimalNumber,
        # The ID of the last Transaction created for the Account.
        'lastTransactionID': TransactionID,
        # The details of the Trades currently open in the Account.
        'trades': (Array[TradeSummary]),
        # The details all Account Positions.
        'positions': (Array[Position]),
        # The details of the Orders currently pending in the Account.
        'orders': (Array[Order])}


class AccountChangesobject:
    """An AccountChanges Refactor is used to represent the changes to an Account’s
    Orders, Trades and Positions since a specified Account TransactionID in the past.
    """
    # JSON representation of object
    schema = {
        # The Orders created. These Orders may have been filled, cancelled or
        # triggered in the same period.
        'ordersCreated': (Array[Order]),
        # The Orders cancelled.
        'ordersCancelled': (Array[Order]),
        # The Orders filled.
        'ordersFilled': (Array[Order]),
        # The Orders triggered.
        'ordersTriggered': (Array[Order]),
        # The Trades opened.
        'tradesOpened': (Array[TradeSummary]),
        # The Trades reduced.
        'tradesReduced': (Array[TradeSummary]),
        # The Trades closed.
        'tradesClosed': (Array[TradeSummary]),
        # The Positions changed.
        'positions': (Array[Position]),
        # The Transactions that have been generated.
        'transactions': (Array[Transaction])}


class AccountChangesStateobject:
    """An AccountState Refactor is used to represent an Account’s current price-dependent state. Price-dependent Account state is dependent
    on OANDA’s current Prices, and includes things like unrealized PL, NAV and Trailing Stop Loss Order state.
    """
    # JSON representation of object
    schema = {
        # The total unrealized profit/loss for all Trades currently open in the
        # Account. Represented in the Account’s home currency.
        'unrealizedPL': AccountUnits,
        # The net asset value of the Account. Equal to Account balance +
        # unrealizedPL. Represented in the Account’s home currency.
        'NAV': AccountUnits,
        # Margin currently used for the Account. Represented in the Account’s home
        # currency.
        'marginUsed': AccountUnits,
        # Margin available for Account. Represented in the Account’s home currency.
        'marginAvailable': AccountUnits,
        # The value of the Account’s open positions represented in the Account’s
        # home currency.
        'positionValue': AccountUnits,
        # The Account’s margin closeout unrealized PL.
        'marginCloseoutUnrealizedPL': AccountUnits,
        # The Account’s margin closeout NAV.
        'marginCloseoutNAV': AccountUnits,
        # The Account’s margin closeout margin used.
        'marginCloseoutMarginUsed': AccountUnits,
        # The Account’s margin closeout percentage. When this value is 1.0 or above
        # the Account is in a margin closeout situation.
        'marginCloseoutPercent': DecimalNumber,
        # The value of the Account’s open positions as used for margin closeout
        # calculations represented in the Account’s home currency.
        'marginCloseoutPositionValue': DecimalNumber,
        # The current WithdrawalLimit for the account which will be zero or a
        # positive value indicating how much can be withdrawn from the account.
        'withdrawalLimit': AccountUnits,
        # The Account’s margin call margin used.
        'marginCallMarginUsed': AccountUnits,
        # The Account’s margin call percentage. When this value is 1.0 or above the
        # Account is in a margin call situation.
        'marginCallPercent': DecimalNumber,
        # The price-dependent state of each pending Order in the Account.
        'orders': (Array[DynamicOrderState]),
        # The price-dependent state for each open Trade in the Account.
        'trades': (Array[CalculatedTradeState]),
        # The price-dependent state for each open Position in the Account.
        'positions': (Array[CalculatedPositionState])}


class AccountPropertiesobject:
    """Properties related to an Account.
    """
    # JSON representation of object
    schema = {
        # The Account’s identifier
        'id': AccountID,
        # The Account’s associated MT4 Account ID. This field will not be present
        # if the Account is not an MT4 account.
        'mt4AccountID': integer,
        # The Account’s tags
        'tags': (Array[string])}


class AccountSummaryobject:
    """A summary representation of a client’s Account. The AccountSummary does not
    provide to full specification of pending Orders, open Trades and Positions.
    """
    # JSON representation of object
    schema = {
        # The Account’s identifier
        'id': AccountID,
        # Client-assigned alias for the Account. Only provided if the Account has
        # an alias set
        'alias': string,
        # The home currency of the Account
        'currency': Currency,
        # The current balance of the Account. Represented in the Account’s home
        # currency.
        'balance': AccountUnits,
        # ID of the user that created the Account.
        'createdByUserID': integer,
        # The date/time when the Account was created.
        'createdTime': DateTime,
        # The total profit/loss realized over the lifetime of the Account.
        # Represented in the Account’s home currency.
        'pl': AccountUnits,
        # The total realized profit/loss for the Account since it was last reset by
        # the client. Represented in the Account’s home currency.
        'resettablePL': AccountUnits,
        # The date/time that the Account’s resettablePL was last reset.
        'resettabledPLTime': DateTime,
        # The total amount of commission paid over the lifetime of the Account.
        # Represented in the Account’s home currency.
        'commission': AccountUnits,
        # Client-provided margin rate override for the Account. The effective
        # margin rate of the Account is the lesser of this value and the OANDA
        # margin rate for the Account’s division. This value is only provided if a
        # margin rate override exists for the Account.
        'marginRate': DecimalNumber,
        # The date/time when the Account entered a margin call state. Only provided
        # if the Account is in a margin call.
        'marginCallEnterTime': DateTime,
        # The number of times that the Account’s current margin call was extended.
        'marginCallExtensionCount': integer,
        # The date/time of the Account’s last margin call extension.
        'lastMarginCallExtensionTime': DateTime,
        # The number of Trades currently open in the Account.
        'openTradeCount': integer,
        # The number of Positions currently open in the Account.
        'openPositionCount': integer,
        # The number of Orders currently pending in the Account.
        'pendingOrderCount': integer,
        # Flag indicating that the Account has hedging enabled.
        'hedgingEnabled': boolean,
        # The total unrealized profit/loss for all Trades currently open in the
        # Account. Represented in the Account’s home currency.
        'unrealizedPL': AccountUnits,
        # The net asset value of the Account. Equal to Account balance +
        # unrealizedPL. Represented in the Account’s home currency.
        'NAV': AccountUnits,
        # Margin currently used for the Account. Represented in the Account’s home
        # currency.
        'marginUsed': AccountUnits,
        # Margin available for Account. Represented in the Account’s home currency.
        'marginAvailable': AccountUnits,
        # The value of the Account’s open positions represented in the Account’s
        # home currency.
        'positionValue': AccountUnits,
        # The Account’s margin closeout unrealized PL.
        'marginCloseoutUnrealizedPL': AccountUnits,
        # The Account’s margin closeout NAV.
        'marginCloseoutNAV': AccountUnits,
        # The Account’s margin closeout margin used.
        'marginCloseoutMarginUsed': AccountUnits,
        # The Account’s margin closeout percentage. When this value is 1.0 or above
        # the Account is in a margin closeout situation.
        'marginCloseoutPercent': DecimalNumber,
        # The value of the Account’s open positions as used for margin closeout
        # calculations represented in the Account’s home currency.
        'marginCloseoutPositionValue': DecimalNumber,
        # The current WithdrawalLimit for the account which will be zero or a
        # positive value indicating how much can be withdrawn from the account.
        'withdrawalLimit': AccountUnits,
        # The Account’s margin call margin used.
        'marginCallMarginUsed': AccountUnits,
        # The Account’s margin call percentage. When this value is 1.0 or above the
        # Account is in a margin call situation.
        'marginCallPercent': DecimalNumber,
        # The ID of the last Transaction created for the Account.
        'lastTransactionID': TransactionID}
