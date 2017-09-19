from ..data.json_data import account
from async_v20.definitions.types import Account

def test_account_builds_from_dict():
    account_instance = Account(**account['account'])
    assert type(account_instance) == Account