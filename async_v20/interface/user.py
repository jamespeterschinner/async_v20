from .decorators import endpoint
from ..endpoints.annotations import UserSpecifier
from ..endpoints.user import *

__all__ = ['UserInterface']


class UserInterface(object):
    @endpoint(GETUserSpecifier)
    def get_user_info(self, user_specifier: UserSpecifier):
        """
        Fetch the user information for the specified user. This endpoint is
        intended to be used by the user thyself to obtain their own
        information.

        Args:

            user_specifier: :class:`~async_v20.endpoints.annotations.UserSpecifier`
                The User Specifier

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (userInfo= :class:`~async_v20.UserInfo`)
        """
        pass

    @endpoint(GETExternalInfo)
    def get_external_user_info(self, user_specifier: UserSpecifier):
        """
        Fetch the externally-available user information for the specified user.
        This endpoint is intended to be used by 3rd parties that have been
        authorized by a user to view their personal information.

        Args:

            user_specifier: :class:`~async_v20.endpoints.annotations.UserSpecifier`
                The User Specifier

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (userInfo= :class:`~async_v20.UserInfoExternal`)
        """
        pass
