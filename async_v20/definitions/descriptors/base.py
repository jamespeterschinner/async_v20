class LengthError(Exception):
    def __init__(self, output):
        super().__init__(output)


class IncorrectValue(Exception):
    def __init__(self, output):
        super().__init__(output)


class DescriptorProtocol(object):

    value = None

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __delete__(self, instance, value):
        pass
        # TODO implement this
        # del getattr(instance, self.name)


class Descriptor(DescriptorProtocol):
    typ = None
    example = None
    values = None


    def __new__(cls, value=None, *, name=None):
        if value is not None:
            return cls.typ(value)
        else:
            return super().__new__(cls)

    def type_check(self, value):
        typ = getattr(self, 'typ', None)
        if typ:
            try:
                value = typ(value)
            except ValueError:
                msg = f'{self.name} must be of type {self.typ.__name__}. ' \
                      f'Or {typ.__name__}({value}) returns {typ}. ' \
                      f'Was {type(value)}'
                raise TypeError(msg)
            else:
                return value

    def __set__(self, instance, value):

        value = self.type_check(value)

        if getattr(self, 'example', None):
            try:
                assert len(self.example) == len(value)
            except AssertionError:
                msg = f'{value} does not match length of example {self.example}. Attribute {type(self)}'
                raise LengthError(msg)

        if getattr(self, 'values', None):
            try:
                assert value in self.values
            except AssertionError:
                possible_values = ', '.join(self.values)
                msg = f'{value} must be in {self.values}. Possible values are {possible_values}'
                raise IncorrectValue(msg)

        setattr(instance, self.name, value)
