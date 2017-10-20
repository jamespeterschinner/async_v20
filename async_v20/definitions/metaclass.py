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
    """Used to denote objects that are sent from OANDA in an array.
    Also used to correctly serialize objects.
    """
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

        # This dict allow for camelCase and snake_case to be passed without error
        kwargs = {self.__class__.instance_attributes[key]: value for key, value in kwargs.items()}
        # Bind passed arguments to the generated signature for this class
        bound = signature.bind(self, *args, **kwargs)
        bound.apply_defaults()

        # When assigning attrs to the instance. The passed value is then passed to the argument's annotation
        # Which is basically type checking. In order to do this, we need a list of tuples with:
        # name :- name of attribute
        # annotation :- signature annotation
        # value :- passed value
        annotations = {attr: param.annotation for attr, param in signature.parameters.items()}
        arguments = [(attr, annotations[attr], value) for attr, value in bound.arguments.items()
                     if value is not None and attr != 'self']

        # Instantiate annotations with value and assign to instance
        for name, annotation, value in arguments:
            self._fields.append(name)
            attribute_value = create_attribute(annotation, value)
            setattr(self, name, attribute_value)

    # Update the signature of the class __init__
    __init__.__signature__ = signature
    return __init__


class ORM(type):
    instance_attributes = {}
    json_attributes = {}

    def __new__(mcs, *args, **kwargs):
        class_obj = super().__new__(mcs, *args, **kwargs)


        # async_v20 allows camelCase and snake_case to be used when instantiating objects.
        # arguments passed in camelCase are converted to snake_case prior to attribute assignment.
        # Signatures arguments are also snake_case.
        # when serializing objects attributes must be converted to camelCase,
        # as per OANDA's specification.
        # To achieve this these two dictionary's are created:
        #   instance_attributes :- camelCase & snake_case keys -> snake_case values
        #   json_attributes :- snake_case
        mcs.instance_attributes.update(create_instance_attributes(class_obj))
        mcs.json_attributes.update(create_json_attributes(class_obj))

        # Instrument the class' with descriptors corresponding to OANDA's definitions
        class_obj = assign_descriptors(class_obj)
        # assign the standard __init__ to correctly initialize objects from json
        class_obj.__init__ = auto_assign(class_obj.__init__, create_signature(class_obj))
        # This dictionary is used to create pandas.Series objects. The template ensures that all
        # like objects have same length Series allowing for them to be passed into a dataframe
        class_obj.template = dict.fromkeys(flatten_dict(class_obj._schema))

        # This attribute is used to keep track of subclasses for specialized creation
        class_obj._dispatch = Dispatch(class_obj)

        return class_obj
