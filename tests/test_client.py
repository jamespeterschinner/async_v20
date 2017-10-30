import pytest
from async_v20.client import OandaClient
import os
import re
from async_v20.endpoints.annotations import Authorization
from .echo_server.server import server
from async_v20 import AccountID

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
        path = os.path.abspath(r'../../async_v20/setup.py')
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
    await client.initialize()
    assert client.default_parameters[AccountID] == AccountID('123-123-1234567-123')