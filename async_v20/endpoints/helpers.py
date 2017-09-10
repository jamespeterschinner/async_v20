class DefaultUnits(str):  # Using a class to allow for isinstance checks
    def __new__(cls, string='ALL'):
        return string
