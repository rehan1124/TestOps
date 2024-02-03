import pytest


@pytest.mark.parametrize("arg1, arg2, result", [(2, 2, 4), (3, 3, 9)])
def test_sum(arg1, arg2, result):
    assert arg1 + arg2 == result
