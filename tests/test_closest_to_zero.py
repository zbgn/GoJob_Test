import pytest

from closest_to_zero import closest_to_zero

def test_closest_to_zero():
    assert closest_to_zero([8, 5, 10]) == 5
    assert closest_to_zero([5, 4, -9, 6, -10, -1, 8]) == -1
    assert closest_to_zero([8, 2, 3, -2]) == 2
    assert closest_to_zero([]) == 0
    assert closest_to_zero() == 0