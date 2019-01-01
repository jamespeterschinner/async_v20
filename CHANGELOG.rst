Changelog
=========

7.1.0b0 (01/01/2019)
=======
 - Added guaranteedStopLossOrderRestriction to Instrument definition
 - Added unixTime attribute to orderBook definition
 - Added tags attribute to Instrument definition
 - Added guarateed to StopLossOrder definition
7.0.1b0
=======
- OandaClient.close is now a coroutine

7.0.0b0
=======

- All OrderRequests now require an `instrument` as there first parameter.
  This is to allow correct rounding of decimal numbers to the instruments specification.
- `guaranteed: bool` has been added to Transaction definition.
- Default SinceTransactionID value is now limited to the passed 900 transactions.
- `OandaClient.account()` method will use `get_account_details()` method when default
  `SinceTransactionID` has expired.
- `OandaClient.get_pricing` now accepts an `InstrumentName` for `instruments`


6.2.2b0
=======

- `guaranteed: bool` has been added to Order definition.

6.2.1b0
=======

- Array class lazy instantiates objects
- Model objects with same attributes now compare equal (proving equal DateTime format)
- Improved repr of Array objects
- Improved implementation of `get_instrument`/s, `get_id`
- All Array objects have `get_instrument` and `get_instruments`. Returns either the first or all matching objects
- Removed Model class `_template` attribute as it was obsolete
- Added `get(self, name, default=None)` method to Model to allow for dict like key access.

6.2.0b0
=======

- Changed `get_transactions` method to `get_transaction` (API call can only return one transaction)
- Removed default parameter argument for `get_transaction`.(**transaction_id**) it is a required parameter.
- Made OandaClient.hosts a protected member. Now OandaClient._hosts
- `Array`. **get_instruments()** returns an Array of the same type this is when there is a one to many relationship
  between the instrument and objects the array contains. `Array`. **get_instrument()** Returns the single object
  when there is a one to one relationship. Both methods are mutually exclusive
- All objects now lazy instantiate attribute instances.
- Large refactoring of async_v20.definitions.base

6.1.0b0
=======

- Changed incorrect naming _i_ds to _ids
- Fixed OrderRequest formatting when a OrderRequest instance is passed that defines an instrument.

6.0.2b0
=======

- Fixed InvalidFormatRequest Error when OrderRequest does not define an `instrument` attribute

6.0.1b0
=======

- Fixed incorrect handling of stream response when endpoint returned status 400

6.0.0b0
=======

- Added health API and initialization check
- Fixed stream_transactions. Now returns correct type
- Changed streaming responses keys. Where stream_pricing() returned 'PRICE' or 'HEARTBEAT'
  response now contains 'price' or 'heartbeat'. Like wise stream_transactions() now returns
  'transaction' or 'heartbeat'. This has been done to standardise access to the transaction
  stream response and 'heartbeat' objects. Due to the different types these objects may take.
- Added async_v20.exceptions module
- Added logging to modules

5.0.3b0
=======

- Added default argument to Array.get_id & Array.get_instrument
- Removed default value from get_candles(*count*)

5.0.2b0
=======

- Fixed bug in rest implementation. Positions now update correctly

5.0.1b0
=======

- OandaClient.datetime_format is read only
- OandaClient._instruments is no longer a protected attribute. It is now OandaClient.instruments

5.0.0b0
=======

- DateTime's create pandas.Timestamp's
- Model.dict argument `datetime` is now `datetime_format`. Argument behaviour now
  specifies the representation of times. Either `RFC3339` or `UNIX`. Corresponding `json` argument
  changes the representation of UNIX times to either a `str` or `numpy.int64`
- *Response* .json() accepts `datetime_format` argument string

4.0.0b0
=======

- Changed get_positions to get_position (as method can only close one position)
- _in_context accepts negative units


3.0.0b0
=======

- Array.get_instrument() works with ArrayInstrument
- OandaClient.initialize() gets account instruments
- OandaClient has `format_order_request` attribute
- async_v20.definitions.primitives.Unit has been removed
- PriceValue and Decimal number has additional method `format(precision, min_, max_)`

2.3.0b0
=======

- Updated limit_replace_order() method to expose all arguments
- TransactionID, TradeID & OrderID get stored as integers and cast to strings when creating JSON
  representations
- Added documentation for order API methods


2.2.5b2
=======

- Fixed get_candles default value

2.2.5b1
=======

- RejectTransactions have no required arguments
- API methods now apply default values
- Added undocumented attributes
- Path class has been removed in favour of helper function. Allowing for more useful
  error message on failure.

2.2.5b0
=======

- PriceComponent accepts all combinations of 'M' 'A' 'B'

2.2.4b3
=======

Added attributes to TradeSummary:
    - margin_used


2.2.4b1
=======

Added attributes to TradeReduce:
    - guaranteed_execution_fee

2.2.4b0
=======

Added attributes to Transaction:
    - guaranteed_execution_fee
    - gain_quote_home_conversion_factor
    - loss_quote_home_conversion_factor

Added attributes to TradeOpen:
    - price
    - guaranteed_execution_fee


2.2.3b0
=======

- Added 'margin_used' to Position object.
  (OANDA added new attribute, causing error)
- Added TimeoutError to stream


2.2.2b0
=======

- Added get_position_book and get_order_book API calls

2.2.1b0
=======

- series() method converts both UNIX and RFC3339 time's to pandas.Timestamp 's


2.2.0b0
=======

- Initialization doesn't freeze after failure
- Order methods exposes all arguments

2.1.0b0
=======

- Beta release. At present time client is considered feature full
  with 100% test coverage
- _fields attribute stored on instance not class
- RESTful account() method added
- close_all_trades() method added
- Added replace() method to Model
- Simplified Endpoint decorator (No serial requests)
- Changes close_trades to close_trade (Method can only close one trade)
- Response parser checks HTTP status first
- Added tests

2.0.1a0
=======

- `type` argument is set automatically for subclass that define it
- implementation improvements

2.0.0a0
=======

- async_v20 objects are now immutable (greatly reducing complexity)
- Objects now have a repr
- removed inflection as a dependency
- Higher test coverage

1.1.6a0
=======

- Issue with object serialization not working with lists of Type[str, float, int]

1.1.5a4
=======

- Argument passing

1.1.5a3
=======

- Fix long description on PyPI


1.1.5a0
=======

- method signatures were offset buy 1 argument due to handling of
  'self' parameter. Methods now displaying correct signature


1.1.4a0
=======

- Fixed incorrect annotation on:
- PUTPositionsInstrumentClose
- GETPositionsInstrument


1.1.3a0
=======

- Fixed incorrect annotation on Interface methods
- Fixed argument passing bug caused by false'y evaluation


1.1.2a5
=======

- Added Travis CI
- Added Codecov


1.1.2a4
=======

- Additional documentation

1.1.2a1
=======

- OandaClient.initialize() method is now exposed
- OandaClient is now also a context manager. To automatically close the http session
- Additional documentation


1.1.1a1
=======

- Floating point numbers are rounded to the correct accuracy required for correct
  serialization.

1.1.0a1
=======


- Model.series() returns data in more specific types instead of all 'str'
- OandaClient methods now have correct signature instead of args, kwargs


1.0.1a1
=======

- Fixed code examples in bin directory
