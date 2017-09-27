from functools import wraps

from .helpers import assign_descriptors
from .helpers import create_attribute
from .helpers import create_instance_attributes
from .helpers import create_json_attributes
from .helpers import create_signature
from .helpers import flatten_dict


class JSONArray(object):
    typ = None

    def __new__(cls, data):
        try:
            return [create_attribute(cls.typ, obj) for obj in data]
        except TypeError as e:
            msg = f'FAILED TO CREATE OBJECT: {cls.typ} FROM DATA: {data} DATA TYPE: {type(data)}'
            print(e.args)
            raise Exception(msg)


class Array(type):
    def __new__(mcs, typ):
        return super().__new__(mcs, f'Array_{typ.__name__}', (JSONArray,), {'typ': typ})


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


def auto_assign(func, signature):
    @wraps(func)
    def __init__(self, *args, **kwargs):
        self._fields = []  # Would normally place this is the class. Didn't segment instance attrs though

        # Encapsulates the idea of an argument
        kwargs = {self.__class__.instance_attributes[key]: value for key, value in kwargs.items()}
        bound = signature.bind(self, *args, **kwargs)
        bound.apply_defaults()

        annotations = {attr: param.annotation for attr, param in signature.parameters.items()}
        arguments = ((attr, annotations[attr], value) for attr, value in bound.arguments.items()
                     if value is not None and attr != 'self')

        for name, annotation, value in arguments:
            self._fields.append(name)
            setattr(self, name, create_attribute(annotation, value))

    __init__.__signature__ = signature
    return __init__


class ORM(type):
    instance_attributes = {}
    json_attributes = {}
    def __new__(mcs, *args, **kwargs):
        class_obj = super().__new__(mcs, *args, **kwargs)
        mcs.instance_attributes.update(create_instance_attributes(class_obj))
        mcs.json_attributes.update(create_json_attributes(class_obj))


        class_obj = assign_descriptors(class_obj)
        class_obj.__init__ = auto_assign(class_obj.__init__, create_signature(class_obj))
        class_obj.template = dict.fromkeys(flatten_dict(class_obj._schema))

        # This attribute is used to keep track of subclasses for specialized creation
        class_obj._dispatch = Dispatch(class_obj)

        return class_obj
