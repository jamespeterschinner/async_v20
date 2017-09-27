from ..data.json_data import GETAccountID_response
from async_v20.definitions.types_remove import Account

def test_account_builds_from_dict():
    account_instance = Account(**GETAccountID_response['account'])
    assert type(account_instance) == Account