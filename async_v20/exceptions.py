class AsyncV20Exception(Exception):
    """A base exception for all exceptions in the async_v20 package"""
    pass

class AsyncV20Warning(Warning):
    """A base warning for all warnings in the async_v20 package"""
    pass

class InitializationFailure(AsyncV20Exception):
    """OandaClient Failed to initialize"""
    pass

class ResponseTimeout(AsyncV20Exception):
    """The server took to long to respond"""
    pass

class CloseAllTradesFailure(AsyncV20Exception):
    """Failed to close all trades"""
    pass

class InvalidValue(AsyncV20Exception):
    """A supplied value does not meet the specification
    of valid values"""
    pass

class InvalidFormatArguments(AsyncV20Exception):
    """Arguments to format a DecimalNumber or PriceValue
    are invalid"""
    pass

class IncompatibleValue(AsyncV20Exception):
    """A supplied argument is different than the predefined value"""
    pass

class UnknownKeywordArgument(AsyncV20Warning):
    """A passed keyword argument is not in the objects __init__ signature"""
    pass

class InstantiationFailure(AsyncV20Exception):
    """async_v20 was unable to create an object from the passed arguments"""
    pass

class UnexpectedStatus(AsyncV20Exception):
    """The server returned an unexpected HTTP status"""
    pass

class FailedToCreatePath(AsyncV20Exception):
    """Unable to construct the path for the requested endpoint"""
    pass

class InvalidOrderRequest(AsyncV20Exception):
    """The order request is not with in the instruments specification
    the order is for"""
    pass