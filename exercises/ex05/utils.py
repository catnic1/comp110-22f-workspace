"""List- Utility Functions- Function Skeletons and Implementations!"""
__author__ = "730328111"


def only_evens(numbers: list[int]) -> list[int]:
    """Returns a list of integers, containing only the even elements of the input parameter."""
    i: int = 0 
    numbers_1: list[int] = []
    while i < len(numbers):
        if numbers[i] % 2 == 0: 
            numbers_1.append(numbers[i]) 
        i += 1
    return numbers_1


def concat(input: list[int], input_2: list[int]) -> list[int]:
    """Returns first list, followed by second list."""
    input_3: list[int] = []
    for numbers in input:
        input_3.append(numbers)
    for numbers in input_2:
        input_3.append(numbers)
    return input_3
    

def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Returns a list which is a subset of given list between start and end integer."""
    if len(a_list) == 0 and start > len(a_list) or end <= 0:
        return []
    
    if start < 0:
        start = 0 
    
    if end > len(a_list):
        end = len(a_list)

    i: int = start
    b_list: list[int] = []
    while i < end:
        b_list.append(a_list[i])
        i += 1
    return b_list