import ujson as json
import logging
from ..definitions.base import Specifier, Model, Array
import pandas as pd

logger = logging.getLogger(__name__)

class Response(dict):
    """A response from OANDA.

    Allows dotted attribute access
    """
    def __init__(self, data, status, bool, datetime_format):
        if data:
            super().__init__(data)
        self.status = status
        self.bool = bool
        self.datetime_format = datetime_format

    def __bool__(self):
        """Returns True if response contains data as per the OANDA spec.

        Returns false if a status code not defined in the endpoint spec was returned
        """
        return self.bool

    def __repr__(self):
        keys = ', '.join(self.keys())
        return f'<Status [{self.status}]: {keys}>'

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            msg = f'No such attribute `{name}`'
            raise AttributeError(msg)

    def dict(self, json=False, datetime_format=None):
        """Convert the response to a nested dictionary

        Args:

            json: Convert object attributes to the :term:`JSON` representation

        """
        if json and datetime_format is None:
            datetime_format = self.datetime_format


        def value_to_dict(value):
            if isinstance(value, Model):
                result = value.dict(json, datetime_format)
            elif isinstance(value, Array):
                try:
                    result = [obj.dict(json, datetime_format) for obj in value]
                except AttributeError:
                    result = [obj for obj in value]
            elif isinstance(value, Specifier) and json:
                    # Specifiers need to be strings for JSON
                result = str(value)
            elif isinstance(value, pd.Timestamp) and json:
                result = value.json(datetime_format)
            else:
                result = value
            return result

        return {key: value_to_dict(value) for key, value in self.items()}

    def json(self, datetime_format=None):
        """Return the json equivalent of the response"""
        return json.dumps(self.dict(json=True, datetime_format=datetime_format))
