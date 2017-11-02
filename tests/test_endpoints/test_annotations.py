import random

import pytest

from async_v20.endpoints import annotations


def test_count_only_allows_valid_data():
    with pytest.raises(ValueError):
        annotations.Count(0)

    with pytest.raises(ValueError):
        annotations.Count(5001)

    assert annotations.Count(random.randrange(1, 5001))

    assert int(annotations.Count()) == 500
