import pytest
from contextlib import nullcontext as does_not_raise

from task_1.solution import add, something


@pytest.mark.parametrize(
    ['a', 'b', 'res', 'expectation'],
    [
        (1, 2, 3, does_not_raise()),
        (1, '3', 4, pytest.raises(TypeError)),
        ([2, 3], 3, 8, pytest.raises(TypeError))
    ]
)
def test_strict_add(a, b, res, expectation):
    with expectation:
        assert add(a, b) == res


@pytest.mark.parametrize(
    ['a', 'b', 'c', 'res', 'expectation'],
    (
        ([1, 2], {1: 2, 3: 4}, '1234', 8, does_not_raise()),
        ([], {}, '', 0, does_not_raise()),
        (1, {}, '', 0, pytest.raises(TypeError)),
        ([], '22', '1234', 6, pytest.raises(TypeError)),
        ([], {}, (0,), 1, pytest.raises(TypeError))
    )
)
def test_strict_something(a, b, c, res, expectation):
    with expectation:
        assert something(a, b, c) == res