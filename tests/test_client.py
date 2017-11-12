import os
import re

import pytest

from async_v20 import AccountID
from async_v20.client import OandaClient
from async_v20.endpoints.annotations import Authorization

from .fixtures.client import client
from .fixtures import server as server_module
import time
import asyncio

client = client
server = server_module.server


# prevent pycharm from removing the import


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


def test_oanda_client_constructs_url(client):
    assert client.hosts['REST'](path='test').human_repr() == 'http://127.0.0.1:8080/test'
    assert client.hosts['STREAM'](path='test').human_repr() == 'http://127.0.0.1:8080/test'


@pytest.mark.asyncio
async def test_client_initializes(client, server):
    server.status = 200
    try:
        await client.initialize()
        assert client.default_parameters[AccountID] == AccountID('123-123-1234567-123')
    except:
        assert 0
    finally:
        client.close()
        assert client.session.closed == True


@pytest.mark.asyncio
async def test_client_raises_connection_error_on_initialisation_failure(client, server):
    server_module.status = 400
    print('TEST STATUS', server_module.status)
    with pytest.raises(ConnectionError):
        await client.initialize()


@pytest.mark.asyncio
async def test_aenter_and_aexit(client, server):
    global status
    status = 200
    async with client as client:
        assert client.session.closed == False
    assert client.session.closed == True


@pytest.mark.asyncio
async def test_async_with_initializes(client, server):
    global status
    status = 200
    async with client as client:
        assert client.default_parameters[AccountID] == AccountID('123-123-1234567-123')


@pytest.mark.asyncio
async def test_response_boolean_evaluation(client, server):
    global status
    status = 200
    async with client as client:
        response = await client.list_accounts()
    assert bool(response) == True


@pytest.mark.asyncio
async def test_response_returns_json(client, server):
    global status
    status = 200
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


def test_client_request_limiter_minimum_value(client):
    client.max_requests_per_second = 0
    assert client.max_requests_per_second == 1

@pytest.mark.asyncio
async def test_request_limiter_limits(client, server, event_loop):

    client.max_simultaneous_connections = 0
    client.max_requests_per_second = 1000
    concurrent_requests = 100
    start = time.time()
    async with client as client:
        await asyncio.gather(*[client.list_orders() for _ in range(concurrent_requests)])
    time_taken = time.time() - start
    print(time_taken)
    assert time_taken >= (concurrent_requests/client.max_requests_per_second)