from functools import wraps
from inspect import signature
from .helpers import assign_descriptors
from .attributes import instance_attributes
from .attributes import json_attributes
from .helpers import create_attribute
from .helpers import create_doc_signature


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

        # # When a bass class is called with a 'type' argument, the argument gets passed to the init
        # # The argument must be removed
        # if self.__class__._derived:
        #     args, kwargs, typ = parse_args_for_typ(self.__class__._derived, args, kwargs)

        # This dict allow for camelCase and snake_case to be passed without error
        kwargs = {self.__class__.instance_attributes[key]: value for key, value in kwargs.items()}
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
            print(annotation, value)
            attribute_value = create_attribute(annotation, value)
            setattr(self, name, attribute_value)

    # Update the signature of the class __init__
    __init__.__signature__ = signature
    return __init__



class ORM(type):
    instance_attributes = {}
    json_attributes = {}

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        pass

    def __new__(mcs, *args, **kwargs):
        class_obj = super().__new__(mcs, *args, **kwargs)

        # async_v20 allows camelCase and snake_case to be used when instantiating objects.
        # arguments passed in camelCase are converted to snake_case prior to attribute assignment.
        # Signature arguments are also snake_case.
        # when serializing objects. Attributes must be converted to camelCase,
        # as per OANDA's specification.
        # To achieve this these two dictionary's are created:
        #   instance_attributes :- camelCase & snake_case keys -> snake_case values
        #   json_attributes :- snake_case keys -> camelCase values
        mcs.instance_attributes = instance_attributes
        mcs.json_attributes = json_attributes

        # Instrument the class' with descriptors corresponding to OANDA's definitions
        class_obj = assign_descriptors(class_obj)
        # Create class signature
        sig = signature(class_obj.__init__)
        # assign the standard __init__ to correctly initialize objects from json
        class_obj.__init__ = auto_assign(class_obj.__init__, sig)
        # Create a pretty signature for documentation
        class_obj.__doc__ = create_doc_signature(class_obj, sig)
        # This dictionary is used to create pandas.Series objects. The template ensures that all
        # like objects have same length Series allowing for them to be passed into a dataframe
        class_obj.template = dict.fromkeys(sig.parameters)

        # This attribute is used to keep track of subclasses for specialized creation
        class_obj._dispatch = Dispatch(class_obj)

        # If the new class is derived from a base class we want to
        # add the derived class as an attribute to the bass class for easier access.
        if class_obj._derived:
            # Add the subclass to the parent for easier access
            setattr(class_obj._derived, class_obj.__name__, class_obj)

        return class_obj
