"""Structured Wordle!"""
__author__ = "730328111"

secret: str = "codes"

def contains_char(search: str, single: str) -> bool:
    """Generates a boolean to check if second parameter is found in first parameter."""
    assert len(single) == 1
    i: int = 0 
    while i < len(search):
        if search[i] == single:
            return True 
        i = i + 1
    return False 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret: str) -> str:
    """Generates a str to test for yellow or white codification."""
    assert len(guess) == len(secret)
    i: int = 0 
    emoji: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX 
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX 
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji

def input_guess(guess: int) -> str:
    """Given an integer of a guess, will prompt user to provide a guess of expected length."""
    word: str = input(f"Enter a {guess} character word: ")
    while len(word) != guess:
        word = input((f"That wasn't {guess} chars! Try again: "))
    
    return word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 0
    guess: str = "codes"
    is_one: bool = False
    while i < 6 and is_one is False:
        print(f"=== Turn {i+1}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            is_one = True
            print(f"You won in {i+1}/6 turns!")
        i += 1 
    if is_one is False:
        print(f"X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()