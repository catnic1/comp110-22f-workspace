"""Dictionary for exercise 7!"""
__author__ = "730328111"


def invert(switch: dict[str, str]) -> dict[str, str]:
    """Should invert keys and values."""
    result: dict[str, str] = {}
    for key in switch:
        if switch[key] in result:
            raise KeyError("Key duplicate!")
        result[switch[key]] = key
    return result 


def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns which color appears most frequently and if there is tie, then return the color that appeared in dictionary first."""
    result: dict[str, int] = {}
    max: int = 0 
    best_color: str = ""
    for key in names_colors:
        if names_colors[key] in result:
            result[names_colors[key]] += 1 
        else: 
            result[names_colors[key]] = 1 
    for color in result:
        if result[color] > max:
            max = result[color]
            best_color = color 
    return best_color


def count(frequencies: list[str]) -> dict[str, int]:
    """Each key is a unique value in the given list and each value associated is the count of number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in frequencies:
        if i in result:
            result[i] += 1 
        else:
            result[i] = 1 
    return result 