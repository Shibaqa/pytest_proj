from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], 4, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2, -1) == [2]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3], end=2) == [1, 2]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -1) == [3]