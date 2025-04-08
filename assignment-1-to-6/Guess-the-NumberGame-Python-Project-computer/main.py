"""
Compulsory Project to be Submitted by the Students
PROJECTS/projects_to_be_submitted_by_students/readme.md
Project 2: Guess the Number Game Python Project (computer)

"""
import random

print("Project 2: Guess the Number Game Python Project (computer)")
def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0  
    while user_guess != random_number:   
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess < random_number:
            print("Sorry, Too low! Try again.")
        elif user_guess > random_number:
            print("Sorry, Too high! Try again.")
    print(f"Yay! Congratulations! You guessed the number {random_number} correctly! 🎉")

guess(10)
