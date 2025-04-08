import random
"""
This Python code is a simple game in which the computer tries to guess a number that the user has in mind, within a given range. 
The user provides feedback to guide the computer towards the correct guess.

"""
# Number Guessing Game

print("Welcome to the Number Guessing Game!")
print("************************************")
print("Keep a no in your mind between 1 and 100. Computer will try to guess it.")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    
    while feedback != 'c' and low != high:  
        guess = random.randint(low, high)  # Only call random.randint once
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower() 
        
        if feedback == 'h': 
            high = guess - 1
        elif feedback == 'l': 
            low = guess + 1
    
    print(f"Yay, the computer guessed your number, {guess}, correctly!")

computer_guess(1000)
# The computer will guess a number between 1 and x  
