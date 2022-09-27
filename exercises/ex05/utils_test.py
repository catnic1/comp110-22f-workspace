"""List- Utility Functions- Unit Tests!"""
__author__ = "730328111"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_1() -> None:
    numbers: list[int] = []
    assert only_evens(numbers) == [] 


def test_only_evens_2() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    assert only_evens(numbers) == [2, 4]


def test_only_evens_3() -> None: 
    numbers: list[int] = [1, 8, 10, 12, 14, 16]
    assert only_evens(numbers) == [8, 10, 12, 14, 16]


def test_concat_1() -> None:
    input: list[int] = []
    input_2: list[int] = []
    assert concat(input, input_2) == []


def test_concat_2() -> None:
    input: list[int] = [1, 2]
    input_2: list[int] = [2, 1]
    assert concat(input, input_2) == [1, 2, 2, 1]


def test_concat_3() -> None:
    input: list[int] = [4, 3, 2, 1]
    input_2: list[int] = [6, 7, 8]
    assert concat(input, input_2) == [4, 3, 2, 1, 6, 7, 8]


def test_sub_1() -> None:
    a_list: list[int] = []
    start: int = 0
    end: int = 0
    assert sub(a_list, start, end) == [] 


def test_sub_2() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [20, 30]


def test_sub_3() -> None:
    a_list: list[int] = [10, 15, 20, 25, 30]
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == [15, 20, 25]