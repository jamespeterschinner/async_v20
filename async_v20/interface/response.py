import ujson as json
from operator import itemgetter

class Response(dict):
    """A response from OANDA.

    Data is accessed as per a standard dictionary
    """
    def __init__(self, data, status, bool):
        super().__init__(data)
        self.status = status
        self.bool = bool

    def __bool__(self):
        """Returns True if response contains data as per the OANDA spec.

        Returns false if a status code not defined in the endpoint spec was returned
        """
        return self.bool

    def __repr__(self):
        return f'<Status [{self.status}]: {", ".join(self.keys())}>'

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError("No such attribute: " + name)

    def dict(self, json=False):

        def value_to_dict(value):
            try:
                # If value is an Model object
                result = value.dict(json)
            except AttributeError:
                try:
                    result = [obj.dict(json) for obj in value]
                except (AttributeError, TypeError):
                    result = value
            return result

        return {key: value_to_dict(value) for key, value in self.items()}

    def json(self):
        """Return the json equivalent of the response"""
        return json.dumps(self.dict(json=True))
