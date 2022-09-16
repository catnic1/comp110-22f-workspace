"""Utility Functions: Lists!"""
__author__ = "730328111"


def all(numbers: list[int], one_number: int) -> bool:
    if len(numbers) == 0:
        return False 
    
    i: int = 0 
    while i < len(numbers): 
        if numbers[i] != one_number: 
            return False
        i += 1 
    return True  # return True only if all numbers match the indicated number. 
 

def max(input: list[int]) -> int:   # Return the largest number in the list.
    if len(input) == 0:
        raise ValueError("max() arg is an empty List") 
    
    max: int = -999 
    i: int = 0 
    while i < len(input):
        if input[i] > max: 
            max = input[i]
        i += 1
    
    return max 


def is_equal(digits: list[int], values: list[int]) -> bool: 
    i: int = 0 
    while i < len(digits): 
        if digits[i] != values[i]: 
            return False 
        i += 1 
    
    return True  # Return True only if the 2 lists are equal at each indices. 