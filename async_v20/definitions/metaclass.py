from .helpers import _create_signature
from .helpers import _assign_descriptors
from .helpers import _create_arg_lookup
from functools import wraps


def _set_attribute(self, attr, value, obj):
    if not isinstance(obj, ORM):
        setattr(self, attr, value)
    else:
        setattr(self, attr, obj(**value))


def _set_kwargs(self, kwargs):
    for attr, value in kwargs.items():
        obj = self.__class__._arg_lookup[attr]
        print(obj)
        _set_attribute(self, attr, value, obj)
    return self


def _set_args(self, args):
    for index, value in enumerate(args):
        obj = self.__class__._arg_lookup[index]
        attr = self.__class__._arg_lookup.reverse_lookup(index)
        _set_attribute(self, attr, value, obj)
    return self


class ORM(type):
    schema = {}

    def __new__(cls, *args, **kwargs):
        class_obj = super().__new__(cls, *args, **kwargs)
        class_obj = _create_arg_lookup(_assign_descriptors(class_obj))
        init_sig = _create_signature(class_obj)

        def auto_assign(init):
            @wraps(init)
            def wrapper(self, *args, **kwargs):
                bound = init_sig.bind(*args, **kwargs)
                bound.apply_defaults()
                _set_kwargs(_set_args(self, args), kwargs)

            wrapper.__signature__ = init_sig
            return wrapper

        class_obj.__init__ = auto_assign(class_obj.__init__)
        return class_obj


class Model(metaclass=ORM):
    pass

