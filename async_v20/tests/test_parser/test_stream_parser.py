import pytest
from async_v20.definitions.types import Price
from async_v20.endpoints.pricing import GETPricingStream
from async_v20.interface.parser import _stream_parser

from ..data.stream_data import price_bytes


async def async_generator():
    while True:
        yield price_bytes


class TestResponse:
    content = async_generator()
    status = 200

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.mark.asyncio
async def test_response_generator():
    data = (i async for i in async_generator())
    result = []
    result.append(await data.asend(None))
    result.append(await data.asend(None))
    assert result == [price_bytes, price_bytes]


@pytest.mark.asyncio
async def test_stream_parser_creates_price_object():
    async_gen = _stream_parser(TestResponse(), GETPricingStream)
    iteration = await async_gen.asend(None)
    assert type(iteration.get('PRICE')) == Price
