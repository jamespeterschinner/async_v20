class ClientPrice(object):
    """Client price for an Account.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The list of prices and liquidity available on the Instrument’s bid side.
			    # It is possible for this list to be empty if there is no bid liquidity
			    # currently available for the Instrument in the Account.
			    # 
			    bids : (Array[PriceBucket]),
			    # 
			    # The list of prices and liquidity available on the Instrument’s ask side.
			    # It is possible for this list to be empty if there is no ask liquidity
			    # currently available for the Instrument in the Account.
			    # 
			    asks : (Array[PriceBucket]),
			    # 
			    # The closeout bid Price. This Price is used when a bid is required to
			    # closeout a Position (margin closeout or manual) yet there is no bid
			    # liquidity. The closeout bid is never used to open a new position.
			    # 
			    closeoutBid : (PriceValue),
			    # 
			    # The closeout ask Price. This Price is used when a ask is required to
			    # closeout a Position (margin closeout or manual) yet there is no ask
			    # liquidity. The closeout ask is never used to open a new position.
			    # 
			    closeoutAsk : (PriceValue),
			    # 
			    # The date/time when the Price was created.
			    # 
			    timestamp : (DateTime)
			}
			"""


class Price(object):
    """The specification of an Account-specific Price.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The string “PRICE”. Used to identify the a Price Refactor when found in a
			    # stream.
			    # 
			    type : (string, default=PRICE),
			    # 
			    # The Price’s Instrument.
			    # 
			    instrument : (InstrumentName),
			    # 
			    # The date/time when the Price was created
			    # 
			    time : (DateTime),
			    # 
			    # The status of the Price.
			    # 
			    # 
			    # Deprecated: Will be removed in a future API update.
			    # 
			    status : (PriceStatus, deprecated),
			    # 
			    # Flag indicating if the Price is tradeable or not
			    # 
			    tradeable : (boolean),
			    # 
			    # The list of prices and liquidity available on the Instrument’s bid side.
			    # It is possible for this list to be empty if there is no bid liquidity
			    # currently available for the Instrument in the Account.
			    # 
			    bids : (Array[PriceBucket]),
			    # 
			    # The list of prices and liquidity available on the Instrument’s ask side.
			    # It is possible for this list to be empty if there is no ask liquidity
			    # currently available for the Instrument in the Account.
			    # 
			    asks : (Array[PriceBucket]),
			    # 
			    # The closeout bid Price. This Price is used when a bid is required to
			    # closeout a Position (margin closeout or manual) yet there is no bid
			    # liquidity. The closeout bid is never used to open a new position.
			    # 
			    closeoutBid : (PriceValue),
			    # 
			    # The closeout ask Price. This Price is used when a ask is required to
			    # closeout a Position (margin closeout or manual) yet there is no ask
			    # liquidity. The closeout ask is never used to open a new position.
			    # 
			    closeoutAsk : (PriceValue),
			    # 
			    # The factors used to convert quantities of this price’s Instrument’s quote
			    # currency into a quantity of the Account’s home currency.
			    # 
			    # 
			    # Deprecated: Will be removed in a future API update.
			    # 
			    quoteHomeConversionFactors : (QuoteHomeConversionFactors, deprecated),
			    # 
			    # Representation of how many units of an Instrument are available to be
			    # traded by an Order depending on its postionFill option.
			    # 
			    # 
			    # Deprecated: Will be removed in a future API update.
			    # 
			    unitsAvailable : (UnitsAvailable, deprecated)
			}
			"""


class PriceBucket(object):
    """A Price Bucket represents a price available for an amount of liquidity
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The Price offered by the PriceBucket
			    # 
			    price : (PriceValue),
			    # 
			    # The amount of liquidity offered by the PriceBucket
			    # 
			    liquidity : (integer)
			}
			"""


class PricingHeartbeat(object):
    """A PricingHeartbeat Refactor is injected into the Pricing
    stream to ensure that the HTTP connection remains active.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The string “HEARTBEAT”
			    # 
			    type : (string, default=HEARTBEAT),
			    # 
			    # The date/time when the Heartbeat was created.
			    # 
			    time : (DateTime)
			}
			"""


class QuoteHomeConversionFactors(object):
    """QuoteHomeConversionFactors represents the factors that can be used used to convert
    quantities of a Price’s Instrument’s quote currency into the Account’s home currency.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The factor used to convert a positive amount of the Price’s Instrument’s
			    # quote currency into a positive amount of the Account’s home currency.
			    # Conversion is performed by multiplying the quote units by the conversion
			    # factor.
			    # 
			    positiveUnits : (DecimalNumber),
			    # 
			    # The factor used to convert a negative amount of the Price’s Instrument’s
			    # quote currency into a negative amount of the Account’s home currency.
			    # Conversion is performed by multiplying the quote units by the conversion
			    # factor.
			    # 
			    negativeUnits : (DecimalNumber)
			}
			"""

