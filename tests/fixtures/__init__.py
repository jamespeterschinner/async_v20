import pytest

from .routes import routes
from .static import account_changes_response, account_changes_response_two
from .static import no_open_trades_response
from .static import list_open_trades_response
from .static import list_services_response
from .static import list_services_bad_response

@pytest.fixture
def changes_response_two():
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/changes'): account_changes_response_two})
    yield
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/changes'): account_changes_response})

@pytest.fixture
def all_trades_closed():
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/openTrades'): no_open_trades_response})
    yield
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/openTrades'): list_open_trades_response})

@pytest.fixture
def all_trades_open_closed():
    def list_trades_response():
        yield list_open_trades_response
        yield no_open_trades_response
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/openTrades'): list_trades_response()})
    yield
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/openTrades'): list_open_trades_response})

@pytest.fixture
def services_down():
    routes.update({('GET', '/api/v1/services'): list_services_bad_response})
    yield
    routes.update({('GET', '/api/v1/services'): list_services_response})