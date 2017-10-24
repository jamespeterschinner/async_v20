import pytest
from async_v20.client import OandaClient
import os
import re
from async_v20.endpoints.annotations import Authorization

@pytest.fixture()
def setup():
    with open(os.path.abspath(r'../../async_v20/setup.py'), 'r') as f:
        yield f.read()

@pytest.fixture()
def client():
    oanda_client = OandaClient()
    yield oanda_client
    del oanda_client

def test_oanda_client_has_correct_version(client, setup):
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
    assert client.hosts['REST'](path='test').human_repr() == 'https://api-fxpractice.oanda.com:443/test'
    assert client.hosts['STREAM'](path='test').human_repr() == 'https://stream-fxpractice.oanda.com/test'
