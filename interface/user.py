from .base_entity import EntityDict, BaseEntity
from async_v20.request import Request
from .types import UserInfo
from .types import UserInfoExternal
import ujson as json


class EntitySpec(object):
    """
    The user.EntitySpec wraps the user module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    UserInfo = UserInfo
    UserInfoExternal = UserInfoExternal

    def __init__(self, ctx):
        self.ctx = ctx


    def get_info(
        self,
        userSpecifier,
        **kwargs
    ):
        """
        Fetch the user information for the specified user. This endpoint is
        intended to be used by the user themself to obtain their own
        information.

        Args:
            userSpecifier:
                The User Specifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/users/{userSpecifier}'
        )

        request.set_path_param(
            'userSpecifier',
            userSpecifier
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('userInfo') is not None:
                parsed_body['userInfo'] = \
                    self.ctx.user.UserInfo.from_dict(
                        jbody['userInfo'],
                        self.ctx
                    )

        elif str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "403":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "405":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        #
        # Unexpected response status
        #
        else:
            parsed_body = jbody

        response.body = parsed_body

        return response


    def get_external_info(
        self,
        userSpecifier,
        **kwargs
    ):
        """
        Fetch the externally-available user information for the specified user.
        This endpoint is intended to be used by 3rd parties that have been
        authorized by a user to view their personal information.

        Args:
            userSpecifier:
                The User Specifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/users/{userSpecifier}/externalInfo'
        )

        request.set_path_param(
            'userSpecifier',
            userSpecifier
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('userInfo') is not None:
                parsed_body['userInfo'] = \
                    self.ctx.user.UserInfoExternal.from_dict(
                        jbody['userInfo'],
                        self.ctx
                    )

        elif str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "403":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "405":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        #
        # Unexpected response status
        #
        else:
            parsed_body = jbody

        response.body = parsed_body

        return response

