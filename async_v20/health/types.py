from ..definitions.base import Model, Array
from .primitives import *

class ServiceList(Model):
    """A collection of related services
    """

    def __new__(cls, id: Id, name: Name, description: Description, url: URL):
        return super().__new__(**ServiceList._preset_arguments, **locals())

class ArrayServiceList(Array):
    _contains = ServiceList

class Service(Model):
    """A log of all events that have occurred in the past.
    The current state of a service is represented by the current status of the service."""

    def __new__(cls, id: Id, name: Name, description: Description,
              list: ServiceList, current_event: CurrentEvent, url: URL):
        return super().__new__(**Service._preset_arguments, **locals())

class ArrayService(Array):
    _contains = Service

class Status(Model):
    """The current event of a status"""

    def __new__(cls, id: Id, name: Name, description: Description, url: URL,
                level: Level, image: Image, default: Default):
        return super().__new__(**Status._preset_arguments, **locals())

class ArrayStatus(Array):
    _contains = Status

class Event(Model):
    """Anything Interesting that has happened to a Service"""

    def __new__(cls, sid: Sid, message: Message, timestamp: Timestamp,
                url: URL, status: Status, informational: Informational):
        return super().__new__(**Event._preset_arguments, **locals())

class ArrayEvent(Array):
    _contains = Event


