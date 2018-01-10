import pytest
from async_v20 import interface
from inspect import Parameter
import logging
logger = logging.getLogger('async_v20')
logger.disabled = True

@pytest.mark.parametrize('interface_method', [method for cls in (getattr(interface, cls) for cls in interface.__all__)
                                              for method in cls.__dict__.values() if hasattr(method, 'endpoint')])
def test_interface_docstrings_have_all_arguments(interface_method):


    sig_names = {name: value for name, value in interface_method.__signature__.parameters.items()
                 if name != 'self'}
    # Call the wrapped method, we are testing the only thing inside method
    # in this test. So may as well do this to improve coverage
    interface_method.__wrapped__(*list(range(len(sig_names) + 1)))
    for key in sig_names:
        assert key in interface_method.__doc__

    # Due to the interface method only being used for defining the interface to the endpoint and is done
    # by creating an annotated signature, the actually method will never be called. Meaning that tests
    # will never have 100% coverage.

    # The above test is the closest test that resembles the the purpose of the api method, There we will
    # call the method simply to gain test coverage.

    interface_method.__wrapped__(*list(range(len(sig_names) + 1)))  # +1 self
