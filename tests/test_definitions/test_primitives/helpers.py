from async_v20.definitions.base import JSONArray, Model

def get_valid_primitive_data(primitive):
    data = None
    if issubclass(primitive, JSONArray):
        return [get_valid_primitive_data(primitive.typ)]
    elif issubclass(primitive, Model):
        return {attr: get_valid_primitive_data(primitive.__annotations__[attr]) for attr in primitive.template
                if attr in primitive.__new__.__signature__.parameters}

    if issubclass(primitive, (float)):
        data = 14.0
    elif issubclass(primitive, (int)):
        data = 123456789
    elif issubclass(primitive, (str)):
        try:
            data = primitive.example
        except AttributeError:
            try:
                data = next(iter(primitive.values))
            except AttributeError:
                data = '1'

    return data
