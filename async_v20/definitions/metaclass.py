from collections import namedtuple
from functools import wraps

from .helpers import assign_descriptors
from .helpers import create_signature
from .helpers import flatten_dict


class JSONArray(type):
    def __getitem__(cls, obj):
        class Array(object):

            typ = obj

            def __new__(self, data: list):
                return [self.typ(**json_obj) for json_obj in data]


        return Array

class Array(metaclass=JSONArray):
    pass

class Dispatch(dict):
    """Keep track of the parent class a subclass is derived from"""
    def __init__(self, derived, **kwargs):
        # derived is the parent class
        self.derived = derived
        super().__init__(self, **kwargs)
        self.name = self.__class__.__name__

    def update(self, *args):
        for cls in args[0].values():
            cls._derived = self.derived
        super().update(*args)

class ORM(type):
    _arg_lookup = {}

    def __new__(mcs, *args, **kwargs):
        class_obj = super().__new__(mcs, *args, **kwargs)
        class_obj = assign_descriptors(class_obj)
        init_sig = create_signature(class_obj._schema)
        class_obj.template = dict.fromkeys(flatten_dict(class_obj._schema))

        # This attribute is used to keep track of subclasses for specialized creation
        class_obj._dispatch = Dispatch(class_obj)



        def auto_assign(init):

            @wraps(init)
            def wrapper(self, *args, **kwargs):
                # Encapsulates the idea of an argument
                argument = namedtuple('argument', ['name', 'value', 'annotation'])
                kwargs = {key.lower(): value for key, value in kwargs.items()}
                bound = init_sig.bind(*args, **kwargs)
                bound.apply_defaults()
                bound = bound.arguments.items()
                annotations = (schema_value.typ for schema_value in self._schema.values())
                arguments = [argument(name_value[0], name_value[1], typ)
                             for name_value, typ
                             in (zip(bound, annotations)) if name_value[1]]

                self._fields = []  # Would normally place this is the class. Didn't segment instance attrs though
                for argument in arguments:
                    self._fields.append(argument.name)
                    if isinstance(argument.annotation, ORM):
                        setattr(self, argument.name, argument.annotation(argument.value))
                    else:
                        setattr(self, argument.name, argument.value)

            wrapper.__signature__ = init_sig
            return wrapper

        class_obj.__init__ = auto_assign(class_obj.__init__)
        return class_obj


