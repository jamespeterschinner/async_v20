import pytest
from async_v20 import interface


@pytest.mark.parametrize('interface_method', [method for cls in (getattr(interface, cls) for cls in interface.__all__)
                                              for method in cls.__dict__.values() if hasattr(method, 'endpoint')])
def test_interface_docstrings_have_all_arguments(interface_method):

    sig_names = dict(interface_method.__signature__.parameters)
    # Call the wrapped method, we are testing the only thing inside method
    # in this test. So may as well do this to improve coverage
    interface_method.__wrapped__(*list(range(len(sig_names)+ 1)))
    print(sig_names)
    for key in sig_names:
        assert key in interface_method.__doc__
