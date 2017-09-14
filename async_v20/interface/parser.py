from ..endpoints.other_responses import other_responses
from ..endpoints.annotations import LastTransactionID
from ..helpers import sleep


async def _parse_response(self, response, endpoint):
    async with response as resp:
        status = resp.status
        headers = resp.raw_headers
        body = await resp.json()

    print(f'RESPONSE STATUS: {status}')

    # Update client headers. Such as lastTransactionID and the like
    for key, value in headers:
        self.default_parameters['key'] = value


    try:
        response_schema = endpoint.responses[status]  # look up the template to process the data
    except KeyError:
        response_schema = other_responses[status]  # See if a response status is an error code

    async def create_objects(key, objs):
        await sleep()
        typ = response_schema.get(key)

        async def build(obj):
            await sleep()
            try:
                obj = typ(**obj)
            except AttributeError:
                pass
            finally:
                return obj

        if isinstance(objs, list):
            objs = [await build(obj) for obj in objs]

        return key, objs  # change here to typ in you'd like the class def as the key

    class Response(object):
        """Object to assign attributes to"""

        @classmethod
        async def create(cls, body):
            class_instance = cls()
            for key, data in body.items():
                attr, value = await create_objects(key, data)
                setattr(class_instance, attr, value)
                if attr == 'lastTransactionID':
                    self.default_parameters.update({LastTransactionID: value})
            return class_instance

    return await Response.create(body)
