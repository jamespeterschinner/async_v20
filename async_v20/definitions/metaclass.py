from asyncio import sleep
from inspect import signature, _empty
from .helpers import _create_signature
from .helpers import _assign_descriptors
from .helpers import _create_arg_lookup
from .descriptors.base import Descriptor
from functools import wraps

class SchemaValue(object):
    def __init__(self, typ, default=_empty, required=False, deprecated=False):
        self.typ = typ
        self.default = default
        self.required = required
        self.deprecated = deprecated


boolean = bool
integer = int
string = str
deprecated = None

class ORM(type):

    schema = {}

    def __new__(cls, *args, **kwargs):
        class_obj = super().__new__(cls, *args, **kwargs)
        init_sig = _create_signature(cls)
        class_obj = _create_arg_lookup(_assign_descriptors(cls))

        def auto_assign(init):
            @wraps(init)
            def wrapper(self, *args, **kwargs):
                bound = init_sig.bind(*args, **kwargs)
                bound.apply_defaults()

                for attribute, value in kwargs.items():
                    typ = self._arg_lookup[attribute]
                    if issubclass(typ, Model):
                        if callable(typ):
                            setattr(self, attribute, typ(**value))
                    else:
                        setattr(self, attribute, value)

                for

            wrapper.__signature__ = init_sig
            return wrapper

        class_obj.__init__ = auto_assign(class_obj.__init__)
        return class_obj


class Model(metaclass=ORM):



    @classmethod
    async def from_dict(cls, data, ctx):

        async def string_to_decimal(key, value):
            typ = cls.attribute_types.get(key, None)
            try:
                if float in typ.typ:
                    value = ctx.convert_decimal_number(value)
            except AttributeError:
                sleep(0)
            finally:
                return key, value

        data = dict([await string_to_decimal(key, value) for key, value in data.items()])
        return cls(**data)
