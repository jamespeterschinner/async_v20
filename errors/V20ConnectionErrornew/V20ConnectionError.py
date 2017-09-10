class V20ConnectionError(Exception):
    """
    A V20ConnectionError is raised when a connection to the V20 REST 
    server was not possible.
    """
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "Connection to v20 REST server at {} failed".format(
            self.url
        )


