class Candlestick(object):
    """The Candlestick representation
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The start time of the candlestick
			    # 
			    time : (DateTime),
			    # 
			    # The candlestick data based on bids. Only provided if bid-based candles
			    # were requested.
			    # 
			    bid : (CandlestickData),
			    # 
			    # The candlestick data based on asks. Only provided if ask-based candles
			    # were requested.
			    # 
			    ask : (CandlestickData),
			    # 
			    # The candlestick data based on midpoints. Only provided if midpoint-based
			    # candles were requested.
			    # 
			    mid : (CandlestickData),
			    # 
			    # The number of prices created during the time-range represented by the
			    # candlestick.
			    # 
			    volume : (integer),
			    # 
			    # A flag indicating if the candlestick is complete. A complete candlestick
			    # is one whose ending time is not in the future.
			    # 
			    complete : (boolean)
			}
			"""


class CandlestickData(object):
    """The price data (open, high, low, close) for the Candlestick representation.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The first (open) price in the time-range represented by the candlestick.
			    # 
			    o : (PriceValue),
			    # 
			    # The highest price in the time-range represented by the candlestick.
			    # 
			    h : (PriceValue),
			    # 
			    # The lowest price in the time-range represented by the candlestick.
			    # 
			    l : (PriceValue),
			    # 
			    # The last (closing) price in the time-range represented by the
			    # candlestick.
			    # 
			    c : (PriceValue)
			}
			"""


class OrderBook(object):
    """The representation of an instrument’s order book at a point in time
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The order book’s instrument
			    # 
			    instrument : (InstrumentName),
			    # 
			    # The time when the order book snapshot was created.
			    # 
			    time : (DateTime),
			    # 
			    # The price (midpoint) for the order book’s instrument at the time of the
			    # order book snapshot
			    # 
			    price : (PriceValue),
			    # 
			    # The price width for each bucket. Each bucket covers the price range from
			    # the bucket’s price to the bucket’s price + bucketWidth.
			    # 
			    bucketWidth : (PriceValue),
			    # 
			    # The partitioned order book, divided into buckets using a default bucket
			    # width. These buckets are only provided for price ranges which actually
			    # contain order or position data.
			    # 
			    buckets : (Array[OrderBookBucket])
			}
			"""


class OrderBookBucket(object):
    """The order book data for a partition of the instrument’s prices.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The lowest price (inclusive) covered by the bucket. The bucket covers the
			    # price range from the price to price + the order book’s bucketWidth.
			    # 
			    price : (PriceValue),
			    # 
			    # The percentage of the total number of orders represented by the long
			    # orders found in this bucket.
			    # 
			    longCountPercent : (DecimalNumber),
			    # 
			    # The percentage of the total number of orders represented by the short
			    # orders found in this bucket.
			    # 
			    shortCountPercent : (DecimalNumber)
			}
			"""


class PositionBook(object):
    """The representation of an instrument’s position book at a point in time
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The position book’s instrument
			    # 
			    instrument : (InstrumentName),
			    # 
			    # The time when the position book snapshot was created
			    # 
			    time : (DateTime),
			    # 
			    # The price (midpoint) for the position book’s instrument at the time of
			    # the position book snapshot
			    # 
			    price : (PriceValue),
			    # 
			    # The price width for each bucket. Each bucket covers the price range from
			    # the bucket’s price to the bucket’s price + bucketWidth.
			    # 
			    bucketWidth : (PriceValue),
			    # 
			    # The partitioned position book, divided into buckets using a default
			    # bucket width. These buckets are only provided for price ranges which
			    # actually contain order or position data.
			    # 
			    buckets : (Array[PositionBookBucket])
			}
			"""


class PositionBookBucket(object):
    """The position book data for a partition of the instrument’s prices.
    """

    # JSON representation of object
    schema = """
			{
			    # 
			    # The lowest price (inclusive) covered by the bucket. The bucket covers the
			    # price range from the price to price + the position book’s bucketWidth.
			    # 
			    price : (PriceValue),
			    # 
			    # The percentage of the total number of positions represented by the long
			    # positions found in this bucket.
			    # 
			    longCountPercent : (DecimalNumber),
			    # 
			    # The percentage of the total number of positions represented by the short
			    # positions found in this bucket.
			    # 
			    shortCountPercent : (DecimalNumber)
			}
			"""

