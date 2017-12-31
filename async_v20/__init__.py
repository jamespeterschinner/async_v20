import logging

from async_v20.client import OandaClient
from async_v20.client import __version__
from async_v20.definitions import *
from async_v20.endpoints.annotations import *

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = __version__
