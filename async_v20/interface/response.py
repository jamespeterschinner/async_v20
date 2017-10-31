import ujson as json

class Response(dict):
    """A response from OANDA.

    Data is accessed as per a standard dictionary
    """


    def __init__(self, data, status,  bool):
        super().__init__(data)
        self.status = status
        self.bool = bool


    def __bool__(self):
        """Returns True if response contains data as per the OANDA spec.

        Returns false if a status code not defined in the endpoint spec was returned
        """
        return self.bool

    def __repr__(self):
        return f'<Status [{self.status}]>'

    def json_dict(self):

        def value_to_json_dict(value):
            try:
                # If value is an Model object
                result = value.json_dict()
            except AttributeError:
                try:
                    result = [obj.json_dict() for obj in value]
                except AttributeError:
                    result = value
            return result

        return {key: value_to_json_dict(value) for key, value in self.items()}

    def json(self):
        """Return the json equivalent of the response"""
        return json.dumps(self.json_dict())