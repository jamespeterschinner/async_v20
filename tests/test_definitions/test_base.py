import pytest
from ..data.json_data import GETAccountID_response
from async_v20.definitions.types import Account
from async_v20.definitions.base import Model
@pytest.fixture
def account():
    result = Account(**GETAccountID_response['account'])
    yield result
    del result

def test_account_has_correct_methods(account):
    assert hasattr(account, 'json_dict')
    assert hasattr(account, 'data')
    assert hasattr(account, 'series')


@pytest.fixture
def test_kwargs():
    kwargs = {'type': 'LIST', 'value': 'TEST_VALUE'}
    yield kwargs
    del kwargs

@pytest.fixture
def test_class():
    class TestClass(Model):
        _dispatch = {'type': 'LIST'}
    test_cls = TestClass
    yield test_cls
    del test_cls


def test_base_dispatch_works_correctly():
    pass