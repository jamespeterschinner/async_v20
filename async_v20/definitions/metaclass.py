from asyncio import sleep
from inspect import signature,
from .helpers import _create_signature
from .helpers import _assign_descriptors
from .descriptors.base import Descriptor
from functools import wraps

boolean = bool
integer = int
string = str
deprecated = None

class ORM(type):

    schema = {}

    def __new__(cls, *args, **kwargs):
        class_obj = super().__new__(cls, *args, **kwargs)
        init_sig = _create_signature(cls.schema)
        class_obj = _assign_descriptors(cls)

        def auto_assign(init):
            @wraps(init)
            def wrapper(self, *args, **kwargs):
                init_sig
                for attribute, value in kwargs.items():
                    typ = self.attribute_types[attribute]
                    if issubclass(typ, Model):
                        if callable(typ):
                            setattr(self, attribute, typ(**value))

                    else:
                        setattr(self, attribute, value)

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
