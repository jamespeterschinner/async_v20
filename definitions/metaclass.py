from asyncio import sleep
from inspect import signature, _empty, Signature
from .descriptors.base import Descriptor
from functools import wraps


class ORM(type):
    def __new__(cls, *args, **kwargs):
        print('creating class')
        class_obj = super().__new__(cls, *args, **kwargs)
        init_sig = signature(class_obj.__init__)
        attribute_types = {param.name: param.annotation
                           for param
                           in init_sig.parameters.values()
                           if param.name != 'self'}

        for attribute, typ in attribute_types.items():
            if issubclass(typ, Descriptor):
                setattr(class_obj, attribute, typ())

        def auto_assign(init):
            @wraps(init)
            def wrapper(self, *args, **kwargs):
                for attribute, value in kwargs.items():
                    typ = self.attribute_types[attribute]
                    if issubclass(typ, Structure):
                        if callable(typ):
                            setattr(self, attribute, typ(**value))

                    else:
                        setattr(self, attribute, value)

            wrapper.__signature__ = init_sig
            return wrapper

        class_obj.__init__ = auto_assign(class_obj.__init__)
        class_obj.attribute_types = attribute_types
        class_obj._properties = list(init_sig.parameters.keys())[1:]
        return class_obj


class TypeModel(metaclass=ORM):
    _summary_format = ''
    # Format string used when generating a name for this object
    _name_format = ''

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
