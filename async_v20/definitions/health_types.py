from .base import Model, Array


class ServiceList(Model):
    """A collection of related services
    """

    def __init__(self, id: str, name: str, description: str, url: str):
        Model.__init__(**locals())


class ArrayServiceList(Array, contains=ServiceList):
    pass


class Status(Model):
    """The current event of a status"""

    def __init__(self, id: str, name: str, description: str, url: str,
                level: str, image: str, default: bool):
        Model.__init__(**locals())


class ArrayStatus(Array, contains=Status):
    pass


class Event(Model):
    """Anything Interesting that has happened to a Service"""

    def __init__(self, sid: str, message: str, timestamp: str,
                url: str, status: Status, informational: bool):
        Model.__init__(**locals())


class ArrayEvent(Array, contains=Event):
    pass


class Service(Model):
    """A log of all events that have occurred in the past.
    The current state of a service is represented by the current status of the service."""

    def __init__(self, id: str, name: str, description: str,
                list: ServiceList, current_event: Event, url: str):
        Model.__init__(**locals())


class ArrayService(Array, contains=Service):
    pass

class Image(Model):
    """An Image to be displayed to the end user.
    """

    def __init__(self, name: str, icon_set: str, url: str):
        Model.__init__(**locals())


class ArrayImage(Array, contains=Image):
    pass
