from .decorators import endpoint
from ..endpoints.health import *
from ..endpoints.health_annotations import *

__all__ = ['HealthInterface']

class HealthInterface(object):

    @endpoint(GETServices, initialize_required=False)
    def list_services(self):
        """List all the services
        """
        pass

    @endpoint(GETService, initialize_required=False)
    def get_service(self, service_id: ServiceID):
        """Get a single service
        """
        pass

    @endpoint(GETServiceLists, initialize_required=False)
    def list_service_lists(self):
        """List all service lists
        """
        pass

    @endpoint(GETServiceList, initialize_required=False)
    def get_service_list(self, service_list_id: ServiceListID):
        """Get a single service list
        """
        pass

    @endpoint(GETEvents, initialize_required=False)
    def list_events(self, service_id: ServiceID):
        """List all events for a service
        """
        pass

    @endpoint(GETCurrentEvent, initialize_required=False)
    def get_current_event(self, service_id: ServiceID):
        """Get the current event for a service
        """
        pass

    @endpoint(GETEvent, initialize_required=False)
    def get_event(self, service_id: ServiceID, event_sid: EventSid):
        """Get an individual event
        """
        pass

    @endpoint(GETStatuses, initialize_required=False)
    def list_statuses(self):
        """List all statuses
        """
        pass

    @endpoint(GETStatus, initialize_required=False)
    def get_status(self, status_id: StatusID):
        """Get an individual status
        """
        pass

    @endpoint(GETImages, initialize_required=False)
    def list_images(self):
        """List all status images
        """
        pass