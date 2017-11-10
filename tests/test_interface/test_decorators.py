from async_v20.interface.decorators import add_signature
from inspect import signature

def test_add_signature():
    """Ensure that the add_signature decorator indeed adds the signature"""

    class ObjWithSig:
        def __new__(cls, arg_1, arg_2, arg_3):
            super().__new__(cls)

    @add_signature(ObjWithSig)
    def wrap_function(*args, **kwargs):
        pass

    assert wrap_function.__signature__ == signature(ObjWithSig.__new__)

    assert wrap_function(1,2,3) == ObjWithSig(1,2,3)