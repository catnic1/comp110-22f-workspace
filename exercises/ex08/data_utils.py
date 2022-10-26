"""Dictionary related utility functions."""

__author__ = "730328111"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
<<<<<<< HEAD
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
=======
    result: list[dict[str,str]] = []
    
    file_handle = open(filename, "r", encoding = "utf8")
>>>>>>> c7b5856 (Progress on Exercise 8)
     
    csv_reader = DictReader(file_handle) 

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


<<<<<<< HEAD
def column_values(table: list[dict[str, str]], column: str) -> list[str]:
=======
def column_values(table: list[dict[str,str]], column: str) -> list[str]:
>>>>>>> c7b5856 (Progress on Exercise 8)
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    
    return result


<<<<<<< HEAD
def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
=======
def columnar(row_table: list[dict[str,str]]) -> dict[str, list[str]]:
>>>>>>> c7b5856 (Progress on Exercise 8)
    """Transform a row-oriented table to a columb-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)

    return result


<<<<<<< HEAD
def head(N: dict[str, list[str]], number: int) -> dict[str, list[str]]:
=======
def head(N :dict[str, list[str]], number: int) -> dict[str, list[str]]:
>>>>>>> c7b5856 (Progress on Exercise 8)
    """Produce a column-based table with only the first rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in N:
        new_list: list[str] = []
        for key in N[column]: 
            if len(new_list) < number: 
                new_list.append(key)
            result[column] = new_list
    
    return result 
    
         
def select(dict_1: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce new column based table with only specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = dict_1[column] 
    
    return result


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in dict_1: 
        result[column] = dict_1[column]
    for column in dict_2: 
        if column in result: 
            result[column] += dict_2[column]
        else: 
            result[column] = dict_2[column]

    return result 


def count(frequencies: list[str]) -> dict[str, int]:
    """Each key is a unique value in the given list and each value associated is the count of number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in frequencies:
        if i in result:
            result[i] += 1 
        else:
            result[i] = 1 
    
    return result 