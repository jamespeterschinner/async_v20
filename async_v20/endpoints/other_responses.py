string = str
error_response = {'errorCode': string, 'errorMessage': string}
other_responses = {
    # A "400 Bad Request" response may be returned from the v20 REST API when the client has
    # provided invalid data to be processed.
    400: error_response,
    # A "401 Unauthorized" response may be returned from the v20 REST API when the endpoint being
    # accessed requires the client to be authenticated however the authentication token is invalid
    # or has not been provided.
    401: error_response,
    # A "403 Forbidden" response may be returned from the v20 REST API when the client has provided
    # a token that does not authorize them to perform the action implemented by the API endpoint.
    403: error_response,
    # A "404 Not Found" response may be returned from the v20 REST API when the client is attempting
    # to refer to an entity (Account, Trade, Order, Position, etc.) that does not exist.
    404: error_response,
    # A "405 Method Not Allowed" response may be returned from the v20 REST API when the client is
    # attempting to access an API endpoint with an HTTP method that is not supported.
    405: error_response,
    # A "416 Range Not Satisfiable" response may be returned from the v20 REST API when the client
    # has specified a range (time range or Transaction range) that is invalid or cannot be processed.
    416: error_response,
    # Excess requests will receive HTTP 429 error.
    # This restriction is applied against the requesting IP address.
    429: error_response
}
