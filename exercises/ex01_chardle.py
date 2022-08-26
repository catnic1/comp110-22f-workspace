"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730328111"

word: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters ")
    exit()

if len(character) != 1:
    print("Error: Character must be a single character. ")
    exit()

print("Searching for " + character + " in " + word)

count = 0
if word[0] == character:
    print(character + " found at index 0")
    count = count + 1
if word[1] == character:
    print(character + " found at index 1")
    count = count + 1 
if word[2] == character:
    print(character + " found at index 2")
    count = count + 1 
if word[3] == character:
    print(character + " found at index 3")
    count = count + 1 
if word[4] == character:
    print(character + " found at index 4")
    count = count + 1 

if count > 1:
    print(str(count) + " instances of " + character + " found in " + word)
if count == 1:
    print(str(count) + " instance of " + character + " found in " + word)
if count == 0:
    print("No instances of " + character + " found in " + word)