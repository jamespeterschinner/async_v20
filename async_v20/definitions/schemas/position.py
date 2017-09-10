class CalculatedPositionState(object):
    """The dynamic (calculated) state of a Position
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The Position’s Instrument.
			    # 
			    instrument : (InstrumentName),
			    # 
			    # The Position’s net unrealized profit/loss
			    # 
			    netUnrealizedPL : (AccountUnits),
			    # 
			    # The unrealized profit/loss of the Position’s long open Trades
			    # 
			    longUnrealizedPL : (AccountUnits),
			    # 
			    # The unrealized profit/loss of the Position’s short open Trades
			    # 
			    shortUnrealizedPL : (AccountUnits)
			}
			"""


class Position(object):
    """The specification of a Position within an Account.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The Position’s Instrument.
			    # 
			    instrument : (InstrumentName),
			    # 
			    # Profit/loss realized by the Position over the lifetime of the Account.
			    # 
			    pl : (AccountUnits),
			    # 
			    # The unrealized profit/loss of all open Trades that contribute to this
			    # Position.
			    # 
			    unrealizedPL : (AccountUnits),
			    # 
			    # Profit/loss realized by the Position since the Account’s resettablePL was
			    # last reset by the client.
			    # 
			    resettablePL : (AccountUnits),
			    # 
			    # The total amount of commission paid for this instrument over the lifetime
			    # of the Account. Represented in the Account’s home currency.
			    # 
			    commission : (AccountUnits),
			    # 
			    # The details of the long side of the Position.
			    # 
			    long : (PositionSide),
			    # 
			    # The details of the short side of the Position.
			    # 
			    short : (PositionSide)
			}
			"""


class PositionSide(object):
    """The representation of a Position for a single direction (long or short).
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # Number of units in the position (negative value indicates short position,
			    # positive indicates long position).
			    # 
			    units : (DecimalNumber),
			    # 
			    # Volume-weighted average of the underlying Trade open prices for the
			    # Position.
			    # 
			    averagePrice : (PriceValue),
			    # 
			    # List of the open Trade IDs which contribute to the open Position.
			    # 
			    tradeIDs : (Array[TradeID]),
			    # 
			    # Profit/loss realized by the PositionSide over the lifetime of the
			    # Account.
			    # 
			    pl : (AccountUnits),
			    # 
			    # The unrealized profit/loss of all open Trades that contribute to this
			    # PositionSide.
			    # 
			    unrealizedPL : (AccountUnits),
			    # 
			    # Profit/loss realized by the PositionSide since the Account’s resettablePL
			    # was last reset by the client.
			    # 
			    resettablePL : (AccountUnits)
			}
			"""

