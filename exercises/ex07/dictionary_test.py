"""Dictionary tests for exercise 7!"""
__author__ = "730328111"

import pytest

from dictionary import invert
from dictionary import favorite_color 
from dictionary import count 


def test_invert_1() -> None:
    """Invert should invert keys and values."""
    switch: dict[str, str] = {}
    assert invert(switch) == {}


def test_invert_2() -> None:
    """Invert should invert keys and values."""
    switch: dict[str, str] = {'apple': 'cat'}
    assert invert(switch) == {'cat': 'apple'}


def test_invert_3() -> None:
    """Invert should invert keys and values."""
    switch: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(switch) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_4() -> None:
    """Invert should invert keys and values."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_1() -> None:
    """Returns which color appears most frequently and if there is tie, then return the color that appeared in dictionary first."""
    names_colors: dict[str, str] = {}
    assert favorite_color(names_colors) == ""


def test_favorite_color_2() -> None:
    """Returns which color appears most frequently and if there is tie, then return the color that appeared in dictionary first."""
    names_colors: dict[str, str] = {"Halle": "green", "Brenda": "red", "Xavier": "green"}
    assert favorite_color(names_colors) == "green"


def test_favorite_color_3() -> None:
    """Returns which color appears most frequently and if there is tie, then return the color that appeared in dictionary first."""
    names_colors: dict[str, str] = {"Nicole": "purple", "Tom": "green", "Lupe": "purple", "Tavo": "green", "Chris": "yellow"}
    assert favorite_color(names_colors) == "purple"


def test_count_1() -> None:
    """Each key is a unique value in the given list and each value associated is the count of number of times that value appeared in the input list."""
    frequencies: list[str] = []
    assert count(frequencies) == {}


def test_count_2() -> None:
    """Each key is a unique value in the given list and each value associated is the count of number of times that value appeared in the input list."""
    frequencies: list[str] = ["one", "two", "one", "three"]
    assert count(frequencies) == {"one": 2, "two": 1, "three": 1}


def test_count_3() -> None:
    """Each key is a unique value in the given list and each value associated is the count of number of times that value appeared in the input list."""
    frequencies: list[str] = ["apple", "pear", "mango", "grape", "apple", "grape", "banana", "pear"]
    assert count(frequencies) == {"apple": 2, "pear": 2, "mango": 1, "grape": 2, "banana": 1}