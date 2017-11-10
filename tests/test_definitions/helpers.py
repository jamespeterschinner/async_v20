from async_v20.definitions.base import Model, Array
from inspect import signature


def create_cls_annotations(cls):
    return {name: param.annotation for
            name, param in
            signature(cls.__new__).parameters.items()}


def get_valid_primitive_data(primitive):
    data = None
    if issubclass(primitive, Array):
        return (get_valid_primitive_data(primitive._contains),)
    elif issubclass(primitive, Model):
        return {attr: get_valid_primitive_data(create_cls_annotations(primitive)[attr])
                for attr in primitive.__new__.__signature__.parameters if
                attr not in 'cls'}

    if issubclass(primitive, (float)):
        data = 14.0
    elif issubclass(primitive, (int)):
        try:
            data = primitive()  # See if the annotation has a default value
        except TypeError:
            pass
        if not data:
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
