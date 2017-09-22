import pytest
from async_v20.definitions.types import StopLossOrderRequest, Account
from async_v20.endpoints.order import POSTOrders
from async_v20.interface.helpers import create_body


@pytest.mark.asyncio
async def test_request_body_is_constructed_correctly():
    stop_loss_order = StopLossOrderRequest(tradeid=1, price=0.8)
    result = await create_body(POSTOrders.request_schema, {'irrelevant': stop_loss_order, 'test': Account()})
    assert result == {"order": {"tradeid": "1", "price": "0.8", "type": "STOP_LOSS", "timeinforce": "GTC",
                                "triggercondition": "DEFAULT"}}
