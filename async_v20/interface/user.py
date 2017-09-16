from .decorators import endpoint
from ..endpoints.user import *


class UserInterface(object):
    @endpoint(GETUserSpecifier)
    def get_user_info(self, userSpecifier: UserSpecifier):
        """
        Fetch the user information for the specified user. This endpoint is
        intended to be used by the user thyself to obtain their own
        information.

        Args:
            userSpecifier:
                The User Specifier

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETExternalInfo)
    def get_external_user_info(self, userSpecifier: UserSpecifier):
        """
        Fetch the externally-available user information for the specified user.
        This endpoint is intended to be used by 3rd parties that have been
        authorized by a user to view their personal information.

        Args:
            userSpecifier:
                The User Specifier

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
