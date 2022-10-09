"""Number Guessing Game!"""
__author__ = "730328111"
 

points: int = 0 
player: str = ""


def main() -> None: 
    """Main function definition & greet player."""
    greet()
    global points 
    global player 
    procedure()
    option: int = 0
    while option < 4:
        print("Choose any of the 3 options. Type 1 if you want to play easy mode. Type 2 if you want to play hard mode. Type 3 if you want to quit.")
        option = int(input("What option are you going to chose? "))
        if option == 1:
            import random
            SECRET: int = random.randint(1, 10)
            points = easy_mode(SECRET)
        if option == 2:
            import random
            SECRET_1: int = random.randint(1, 50)
            points = hard_mode(SECRET_1)
        if option == 3:
            print(f"Okay, goodbye and have a great day! Your adventure points are {points}")
            quit()
        points += 1 


def greet() -> None: 
    """Player is greeted and asked name."""
    global player
    player = input("What is your name? ")
    NAMED_CONSTANT: str = "\U0001F920"
    print(f"Hello {player}, Welcome to the Number Guessing Game! In this game you will play to guess the correct number {NAMED_CONSTANT}!")


def procedure() -> None: 
    """Player is asked if they are excited to play the game."""
    global player
    global points
    guess: str = input(f"Alright {player}, are you excited to continue on with game- yes or no? ")
    if guess == "yes":
        print("That's great!")
    else: 
        print("I'm sorry, hopefully you will have a good time anyway!")
    points += 1 


def easy_mode(SECRET: int) -> int:
    """Player is asked the number."""
    global player
    global points
    guess: int = 0
    while guess != SECRET:
        guess = int(input(f"Hi {player}, what number is your guess between 1-10? "))
        if guess == SECRET:
            print("Correct, Congrats!") 
        else:
            print("Not correct, try again!")
        points += 1 
    return points 


def hard_mode(SECRET_1: int) -> int:
    """Player is asked the number."""
    global player
    global points
    guess: int = 0 
    while guess != SECRET_1:
        guess = int(input(f"Hi {player}, what number is your guess between 1-50? "))
        if guess == SECRET_1:
            print("Correct")
        else:
            print("Oops try again!")
        points += 1 
    return points 


if __name__ == "__main__":
    main()