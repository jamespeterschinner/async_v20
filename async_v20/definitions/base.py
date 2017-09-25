import pandas as pd

from .helpers import async_flatten_dict
from .metaclass import *


class Model(metaclass=ORM):
    _schema = {}

    _derived = None

    # More info about this code be found in PEP 487 https://www.python.org/dev/peps/pep-0487/
    def __init_subclass__(cls, **kwargs):
        # super().__init_subclass__(**kwargs)
        dispatch_key = cls._schema.get('type', None)
        if dispatch_key:
            cls._dispatch.update({dispatch_key.default: cls})
        else:
            cls._derived = cls

    def __init__(self, *args, **kwargs):
        "Keeps IDE happy"
        pass

    def __new__(cls, *args, **kwargs):
        if cls._dispatch:
            typ = kwargs.get('type', None)
            if typ:
                return cls._dispatch['type'](*args, **kwargs)
        else:
            return super().__new__(cls)

    def __repr__(self):
        return self.__class__.__name__

    # Recursion might be an issue
    async def json_dict(self):
        async def get_object_fields(attr):
            attr = getattr(self, attr)
            if isinstance(attr, Model):
                attr = await attr.json_dict()
            return str(attr)

        return {attr: await get_object_fields(attr) for attr in self._fields}

    async def data(self):
        return await async_flatten_dict(await self.json_dict())

    async def series(self):
        return pd.Series(dict(self.template, **await self.data()))
