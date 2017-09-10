class ResponseUnexpectedStatus(Exception):
    """
    A ResponseUnexpectedStatus exception is raised when a certain HTTP status
    code is expected in a response however a differend status code has
    been received.
    """
    def __init__(self, response, expected_status):
        self.response = response
        self.expected_status = expected_status

    def __str__(self):
        return "{} {} expected status {}, got {} ({})".format(
            self.response.method,
            self.response.path,
            self.expected_status,
            self.response.status,
            self.response.reason
        )


