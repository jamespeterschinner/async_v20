from ..definitions.base import Model

class Response(dict):

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