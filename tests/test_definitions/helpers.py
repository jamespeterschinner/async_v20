from inspect import signature, _empty
from async_v20.definitions.types import DateTime
from async_v20.definitions.base import Model, Array
from async_v20.endpoints.annotations import Bool, FromTime, ToTime


def create_cls_annotations(cls):
    return {name: param.annotation for
            name, param in
            signature(cls.__init__).parameters.items()}


def get_valid_primitive_data(primitive):
    data = None
    if primitive == _empty:
        return
    elif issubclass(primitive, DateTime): #or primitive == FromTime or primitive == ToTime:
        # Means it is a time
        return '2017-12-19T21:27:45.000000000Z'
    elif issubclass(primitive, Array):
        return (get_valid_primitive_data(primitive._contains),)
    elif issubclass(primitive, Model):
        return {attr: get_valid_primitive_data(create_cls_annotations(primitive)[attr])
                for attr in primitive.__annotations__}
    if issubclass(primitive, (float)):
        data = 14.0
    elif issubclass(primitive, (int)):
        try:
            data = primitive()  # See if the annotation has a default value
        except TypeError:
            data = 123456789
    elif issubclass(primitive, Bool):
        data = primitive()
    # The only valid option here should be a subclass of str
    else:
        print(primitive)
        assert issubclass(primitive, (str))
        try:
            data = primitive.example
        except AttributeError:
            try:
                data = next(iter(primitive.values))
            except AttributeError:
                data = '1'

    return data
