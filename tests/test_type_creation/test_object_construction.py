from ..data.json_data import GETAccountID_response
from ..data.json_data import position_response
from ..data.json_data import order_cancel_transaction_json_dict
from ..data.json_data import example_order
from ..data.json_data import account_example
from ..data.json_data import example_transaction_array
from ..data.json_data import example_trade_array
from async_v20.definitions.types import Account
from async_v20.definitions.types import Position
from async_v20.definitions.types import Instrument
from async_v20.definitions.types import OrderCancelTransaction
from async_v20.definitions.types import ArrayOrder
from async_v20.definitions.types import Account
from async_v20.definitions.types import Order
from async_v20.definitions.types import ArrayTransaction
from async_v20.definitions.types import ArrayTrade
from async_v20.definitions.primitives import TradeSpecifier
from async_v20.definitions.primitives import OrderSpecifier
import pandas as pd
import pytest


def test_account_builds_from_dict():
    account_instance = Account(**GETAccountID_response['account'])
    assert type(account_instance) == Account
    series = account_instance.series()
    assert type(series) == pd.Series


def test_position_builds_from_dict():
    position = Position(**position_response)
    assert type(position) == Position
    series = position.series()
    assert type(series) == pd.Series


def test_order_cancel_transaction_builds_from_dict():
    order_cancel_transaction = OrderCancelTransaction(**order_cancel_transaction_json_dict)
    assert type(order_cancel_transaction) == OrderCancelTransaction
    series = order_cancel_transaction.series()
    assert type(series) == pd.Series


def test_supplying_incorret_preset_argument_raises_value_error():
    order_cancel_transaction_json_dict.update(type='INCORRECT VALUE')
    with pytest.raises(ValueError):
        OrderCancelTransaction(**order_cancel_transaction_json_dict)

def test_passing_empty_list_tuple_to_array_returns_empty_array():
    array_order = ArrayOrder(*[])
    assert type(array_order) == ArrayOrder
    account = Account(orders=[])
    assert type(account.orders) == ArrayOrder
    account = Account(orders=())
    assert type(account.orders) == ArrayOrder

def test_specifiers_can_be_constructed_from_int():
    assert type(TradeSpecifier(1234)) == TradeSpecifier
    assert type(OrderSpecifier(1234)) == OrderSpecifier

def test_order_can_be_constructed_from_example_data():
    assert type(Order(**example_order)) == Order

def test_supplying_incorrect_type_raises_error():
    with pytest.raises(TypeError):
        Order(instrument=Instrument())

def test_account_object_can_be_constructed_from_example():
    assert type(Account(**account_example['account'])) == Account

def test_transaction_array_can_be_constructed_from_example():
    assert type(ArrayTransaction(*example_transaction_array)) == ArrayTransaction

def test_trade_array_can_be_constructed_from_example():
    assert type(ArrayTrade(*example_trade_array)) == ArrayTrade