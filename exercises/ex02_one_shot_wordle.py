"""EX02 - One - Shot Wordle - Loops!"""
__author__ = "730328111"

SECRET: str = "python"

guess: str = input(f"What is your {len(SECRET)}-letter guess? ")

while len(guess) != len(SECRET):
    guess = input((f"That was not {len(SECRET)} letters! Try again: "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0 
emoji: str = ""
while i < len(SECRET):
    if guess[i] == SECRET[i]:
        emoji = emoji + GREEN_BOX
    else:
        wrong_place: bool = False
        variable: int = 0 
        while variable < len(SECRET):
            if SECRET[variable] == guess[i]:
                wrong_place = True 
            variable = variable + 1
        if wrong_place is True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    i = i + 1 
print(emoji)

if (SECRET) == (guess):
    print("Woo! You got it!")
else:
    if len(SECRET) == len(guess):
        print("Not quite. Play again soon!")