class V20Timeout(Exception):
    """
    A V20Timeout is raised when attempting to interract with the V20 REST 
    server has timed out.
    """
    def __init__(self, url, type):
        self.url = url
        self.type = type

    def __str__(self):
        return "v20 REST request to {} has timed out ({})".format(
            self.url,
            self.type
        )


