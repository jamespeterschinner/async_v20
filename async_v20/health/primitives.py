from ..definitions.primitives import Primitive

class CurrentEvent(str, Primitive):
    pass

class Default(str, Primitive):
    pass

class Description(str, Primitive):
    pass

class IconSet(str, Primitive):
    pass

class Id(str, Primitive):
    pass

class Image(str, Primitive):
    pass

class Informational(str, Primitive):
    # Actually a bool
    pass

class Level(str, Primitive):
    pass

class List(str, Primitive):
    pass

class Message(str, Primitive):
    pass

class Name(str, Primitive):
    pass

class Sid(str, Primitive):
    pass

class Status(str, Primitive):
    pass

class Timestamp(str, Primitive):
    pass

class URL(str, Primitive):
    pass