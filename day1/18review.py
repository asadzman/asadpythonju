import pytest
from parameterized import parameterized


@parameterized.expand(
    [
        (2, 2, 4),
        (2, 3, 8),
        (1, 9, 1),
        (0, 9, 0),
    ]
)
def test_power(base, exponent, expected):
    assert base**exponent == expected
