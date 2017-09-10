class LengthError(Exception):
    def __init__(self, output):
        pass

class IncorrectValue(Exception):
    def __init__(self, output):
        pass


class Descriptor(object):
    def __init__(self):
        self.name = self.__class__.__name__

    def __set__(self, instance, value):

        if getattr(self, 'typ', None):
            try:
                assert isinstance(value, self.typ)
            except AssertionError:
                msg = f'{self.name} must be of type {self.typ}. Was {type(value)}'
                raise TypeError(msg)

        if getattr(self, 'example', None):
            try:
                assert len(self.example) == len(value)
            except AssertionError:
                msg = f'{value} does not match length of example {self.example}'
                raise LengthError(msg)

        if getattr(self, 'values', None):
            try:
                assert value in self.values
            except AssertionError:
                possible_values = ', '.join(self.values)
                msg = f'{value} must be in {self.values}. Possible values are {possible_values}'
                raise IncorrectValue(msg)

        instance.value = value

    def __get__(self, instance, value):
        return instance.value

    def __delete__(self, instance, value):
        del instance.value
