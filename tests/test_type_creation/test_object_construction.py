from ..data.json_data import GETAccountID_response, position_response, order_cancel_transaction_json_dict
from async_v20.definitions.types import Account, Position, OrderCancelTransaction, ArrayOrder, Account
from async_v20.definitions.primitives import TradeSpecifier, OrderSpecifier
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