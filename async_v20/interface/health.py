from .decorators import endpoint
from ..endpoints.health import *

__all__ = ['HealthInterface']


class HealthInterface(object):
    @endpoint(GETServices, initialize_required=False)
    def list_services(self):
        """List all the services

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (services=( :class:`~async_v20.definitions.health_types.Service`, ...))

        """
        pass

    @endpoint(GETService, initialize_required=False)
    def get_service(self, service_id: ServiceID):
        """Get a single service

        Args:

            service_id: :class:`~async_v20.endpoints.annotations.ServiceID`
                Name of the service to get

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (Service= :class:`~async_v20.definitions.health_types.Service`)

        """
        pass

    @endpoint(GETServiceLists, initialize_required=False)
    def list_service_lists(self):
        """List all service lists

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (lists=( :class:`~async_v20.definitions.health_types.ServiceList`, ...))
        """
        pass

    @endpoint(GETServiceList, initialize_required=False)
    def get_service_list(self, service_list_id: ServiceListID):
        """Get a single service list

        Args:

            service_list_id: :class:`~async_v20.endpoints.annotations.ServiceListID`
                The service list to get.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (lists= :class:`~async_v20.definitions.health_types.ServiceList`)
        """
        pass

    @endpoint(GETEvents, initialize_required=False)
    def list_events(self, service_id: ServiceID):
        """List all events for a service

        Args:

            service_id: :class:`~async_v20.endpoints.annotations.ServiceID`
                The service to get events for.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (lists=( :class:`~async_v20.definitions.health_types.Event`,...))
        """
        pass

    @endpoint(GETCurrentEvent, initialize_required=False)
    def get_current_event(self, service_id: ServiceID):
        """Get the current event for a service

        Args:

            service_id: :class:`~async_v20.endpoints.annotations.ServiceID`
                The service to get the current event for

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (Event= :class:`~async_v20.definitions.health_types.Event`)
        """
        pass

    @endpoint(GETEvent, initialize_required=False)
    def get_event(self, service_id: ServiceID, event_sid: EventSid):
        """Get an individual event

        Args:

            service_id: :class:`~async_v20.endpoints.annotations.ServiceID`
                The service to event for
            event_sid: :class:`~async_v20.endpoints.annotations.EventSid`
                The event to get from the specified service

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (Event= :class:`~async_v20.definitions.health_types.Event`)
        """
        pass

    @endpoint(GETStatuses, initialize_required=False)
    def list_statuses(self):
        """List all statuses

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (statuses=( :class:`~async_v20.definitions.health_types.Event`, ...))
        """
        pass

    @endpoint(GETStatus, initialize_required=False)
    def get_status(self, status_id: StatusID):
        """Get an individual status

        Args:

            status_id: :class:`~async_v20.endpoints.annotations.StatusID`
                The status to get

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (Status= :class:`~async_v20.definitions.health_types.Status`)
        """
        pass

    @endpoint(GETImages, initialize_required=False)
    def list_images(self):
        """List all status images

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (images=( :class:`~async_v20.definitions.health_types.Image`, ...))
        """
        pass
