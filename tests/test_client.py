import pytest
from async_v20.client import OandaClient
import os
import re
from async_v20.endpoints.annotations import Authorization
from .server.server import server
from async_v20 import AccountID
from .server.static import list_accounts_response
from .server.static import get_account_details_response
from .server.static import get_pricing_response
from .test_interface.helpers import order_dict
import ujson as json
#prevent pycharm from removing the import
server = server

def test_server_works(server):
    print(server)
    assert server

@pytest.fixture()
def client():
    oanda_client = OandaClient(rest_host='127.0.0.1', rest_port=8080, rest_scheme='http',
                               stream_host='127.0.0.1', stream_port=8080, stream_scheme='http')
    yield oanda_client
    del oanda_client

def test_oanda_client_has_correct_version(client):
    try:
        path = r'C:\Users\James\PycharmProjects\async_v20\setup.py'
        print(path)
        with open(path, 'r') as f:
            setup = f.read()
    except FileNotFoundError as e:
        print(e)
    else:
        setup_version = re.findall(r"(?<=version\s=\s').*?(?='\n)", setup)[0]
        assert setup_version == client.version

def test_oanda_client_finds_token():
    os.environ['OANDA_TOKEN'] = 'test_environ_token'
    client = OandaClient()
    assert client.default_parameters[Authorization] == 'Bearer test_environ_token'

def test_oanda_client_accepts_token():
    client = OandaClient(token='test_token')
    assert client.default_parameters[Authorization] == 'Bearer test_token'

def test_oanda_client_has_application_name(client):
    assert client.application == 'async_v20'

def test_oanda_client_constructs_url(client):
    assert client.hosts['REST'](path='test').human_repr() == 'http://127.0.0.1:8080/test'
    assert client.hosts['STREAM'](path='test').human_repr() == 'http://127.0.0.1:8080/test'

@pytest.mark.asyncio
async def test_client_initializes(client, server):
    try:
        await client.initialize()
        assert client.default_parameters[AccountID] == AccountID('123-123-1234567-123')
    except:
        assert 0
    finally:
        client.close()
        assert client.session.closed == True

@pytest.mark.asyncio
async def test_aenter_and_aexit(client, server):
    async with client as client:
        assert client.session.closed == False
    assert client.session.closed == True

@pytest.mark.asyncio
async def test_async_with_initializes(client, server):
    async with client as client:
        assert client.default_parameters[AccountID] == AccountID('123-123-1234567-123')

@pytest.mark.asyncio
async def test_response_boolean_evaluation(client, server):
    async with client as client:
        response = await client.list_accounts()
    assert bool(response) == True


@pytest.mark.asyncio
async def test_response_returns_json(client, server):
    async with client as client:
        accounts = await client.list_accounts()
        account_details = await client.get_account_details()
        pricing = await client.get_pricing()

    assert accounts.json_dict()
    assert account_details.json_dict()
    assert pricing.json_dict()


@pytest.mark.asyncio
async def test_enter_causes_warning(client, server, capsys):
    with client as client:
        assert capsys.readouterr()[0] == 'Warning: <with> used rather than <async with>\n'
