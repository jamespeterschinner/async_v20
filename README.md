# async_v20

An asynchronous client application for the OANDA's v20 Rest Api. 
 
The package aims to provide an async version of the OANDA v20 python wrapper


# Disclaimer 
Losses can exceed investment.

async_v20 and its creator has no affiliation with OANDA. And is not endorsed by OANDA in any manner.

async_v20 is in Alpha stage and has not been tested on a live OANDA account

This package currently does not have full unittest coverage.

# Usage
To install use:

`$ pip install async_v20`

To use async_v20 you must have an account with OANDA.

It is strongly suggested to create a practice account. 

You can register here: https://www.oanda.com/account/login

Once an account has been created you must generate an API TOKEN. 

This is the link to generate an API TOKEN: 
https://www.oanda.com/demo-account/tpa/personal_token

This is an example TOKEN:

26c289810eeede6677e8a04eb4aae282-10b8d4c084035bd815a3a9dcfb36212e

Create an environment variable with the name 'OANDA_TOKEN' (no quotation marks) 
with the previously created API TOKEN as the variable's value. 

async_v20 provides one interface to OANDA'a v20 REST API. This interface is `OandaClient`

it can be imported into you project like this:

`from async_v20.client import OandaClient`

You must instantiate an OandaClient instance. Example:

`oanda_client = OandaClient()`

Methods on the oanda_client object then correspond to OANDA's v20 API

This example code retrieves candles for the AUD/USD currency pair with monthly granularity

    import asyncio
    
    from async_v20 import OandaClient
    
    
    async def candles():
        oanda_client = OandaClient()
        try:
            response = await oanda_client.get_candles('AUD_USD', granularity='M')
        finally:
            oanda_client.session.close()
        return response
    
    
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(candles())
    
    # HTTP response state
    print(response['instrument'])
    
    # JSON data in python dictionary format
    print(response['candles'][0].json_dict())
    
    # pandas Series
    print(response['candles'][0].series())


