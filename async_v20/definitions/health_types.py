from .base import Model, Array


class ServiceList(Model):
    """A collection of related services
    """

    def __new__(cls, id: str, name: str, description: str, url: str):
        return super().__new__(**ServiceList._preset_arguments, **locals())


class ArrayServiceList(Array, contains=ServiceList):
    pass


class Status(Model):
    """The current event of a status"""

    def __new__(cls, id: str, name: str, description: str, url: str,
                level: str, image: str, default: bool):
        return super().__new__(**Status._preset_arguments, **locals())


class ArrayStatus(Array, contains=Status):
    pass


class Event(Model):
    """Anything Interesting that has happened to a Service"""

    def __new__(cls, sid: str, message: str, timestamp: str,
                url: str, status: Status, informational: bool):
        return super().__new__(**Event._preset_arguments, **locals())


class ArrayEvent(Array, contains=Event):
    pass


class Service(Model):
    """A log of all events that have occurred in the past.
    The current state of a service is represented by the current status of the service."""

    def __new__(cls, id: str, name: str, description: str,
                list: ServiceList, current_event: Event, url: str):
        return super().__new__(**Service._preset_arguments, **locals())


class ArrayService(Array, contains=Service):
    pass

class Image(Model):
    """An Image to be displayed to the end user.
    """

    def __new__(cls, name: str, icon_set: str, url: str):
        return super().__new__(**Image._preset_arguments, **locals())


class ArrayImage(Array, contains=Image):
    pass
