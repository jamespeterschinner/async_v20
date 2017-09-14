from .interface import *


class Client(AccountInterface, InstrumentInterface, OrderInterface, PositionInterface, PricingInterface, TradeInterface,
             TransactionInterface, UserInterface):
    """
    A Client encapsulates a connection to OANDA's v20 REST API.
    """
    pass
