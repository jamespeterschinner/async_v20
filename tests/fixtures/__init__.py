import pytest

from .routes import routes
from .static import account_changes_response, account_changes_response_two

@pytest.fixture
def changes_response_two():
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/changes'): account_changes_response_two})
    yield
    routes.update({('GET', '/v3/accounts/123-123-1234567-123/changes'): account_changes_response})
