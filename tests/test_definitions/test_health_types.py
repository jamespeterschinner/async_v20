from ..data.json_data import list_service_lists_response, list_images_response
from async_v20.definitions.health_types import ArrayServiceList, ArrayImage
import json

import logging
logger = logging.getLogger()
logger.disabled = True


def test_array_service_lists_constructs():
    data = json.loads(list_service_lists_response)
    array = ArrayServiceList(*data['lists'])
    for i in array:
        print(i)

def test_array_image_lists_constructs():
    array = ArrayImage(*json.loads(list_images_response)['images'])
    for i in array:
        print(i)