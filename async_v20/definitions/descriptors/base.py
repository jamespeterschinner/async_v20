class LengthError(Exception):
    def __init__(self, output):
        super().__init__(output)


class IncorrectValue(Exception):
    def __init__(self, output):
        super().__init__(output)


class DescriptorProtocol(object):

    value = None
    # def __init__(self, name=None, value=None):
    #     self.value = value
    #     self.name = name
    #     if name is None:
    #         self.name = self.__class__.__name__

    def __set__(self, instance, value):
        self.value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __delete__(self, instance, value):
        del self.value


class Descriptor(DescriptorProtocol):
    typ = None
    example = None
    values = None

    def __new__(cls, value=None):
        if value:
            return cls.typ(value)
        else:
            return super().__new__(cls)

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

        self.value = value
