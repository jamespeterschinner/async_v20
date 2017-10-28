
class Response(dict):

    def json_dict(self):

        def value_to_json_dict(value):
            try:
                # If value is an Model object
                result = value.json_dict()
            except AttributeError:
                if isinstance(value, tuple):
                    # If value is an Array of Model objects
                    result = [obj.json_dict() for obj in value]
                else:
                    result = value
            return result

        return {key: value_to_json_dict(value) for key, value in self.items()}