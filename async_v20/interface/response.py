
class Response(dict):

    async def json_dict(self):

        async def value_to_json_dict(value):
            try:
                # If value is an Model object
                result = await value.json_dict()
            except AttributeError:
                if isinstance(value, list):
                    # If value is an Array of Model objects
                    result = [await obj.json_dict() for obj in value]
                else:
                    result = value
            return result

        return {key: await value_to_json_dict(value) for key, value in self.items()}