from .decorators import endpoint
from ..endpoints.annotations import UserSpecifier
from ..endpoints.user import *


class UserInterface(object):
    @endpoint(GETUserSpecifier)
    def get_user_info(self, user_specifier: UserSpecifier):
        """
        Fetch the user information for the specified user. This endpoint is
        intended to be used by the user thyself to obtain their own
        information.

        Args:
            user_specifier:
                The User Specifier

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETExternalInfo)
    def get_external_user_info(self, user_specifier: UserSpecifier):
        """
        Fetch the externally-available user information for the specified user.
        This endpoint is intended to be used by 3rd parties that have been
        authorized by a user to view their personal information.

        Args:
            user_specifier:
                The User Specifier

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
