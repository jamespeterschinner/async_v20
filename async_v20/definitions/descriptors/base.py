class LengthError(Exception):
    def __init__(self, output):
        super().__init__(output)


class IncorrectValue(Exception):
    def __init__(self, output):
        super().__init__(output)


class DescriptorProtocol(type):

    def __set__(self, instance, value):
        pass
    def __get__(self, instance, owner):
        pass
    def __delete__(self, instance):
        pass

class Descriptor(metaclass=DescriptorProtocol):
    typ = None
    example = None
    values = None

    def __init__(self):
        self.name = self.__class__.__name__

    def __set__(self, instance, value):

        typ = getattr(self, 'typ', None)
        if typ:
            try:
                assert isinstance(value, self.typ)
            except AssertionError:
                try:
                    value = typ(value)
                except ValueError:
                    msg = f'{self.name} must be of type {self.typ.__name__}. ' \
                          f'Or {typ.__name__}({value}) returns {typ}. ' \
                          f'Was {type(value)}'
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

        setattr(instance, self.name, value)

    def __get__(self, instance, value):
        return getattr(instance, self.name, value)

    def __delete__(self, instance, value):
        delattr(instance, self.name)
