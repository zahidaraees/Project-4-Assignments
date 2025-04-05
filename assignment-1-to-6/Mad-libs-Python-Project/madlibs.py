# Mad Libs Game

# Getting user input for Story Template variables
human_name = input("Enter an human name: ")
place = input("Enter his favorite place: ")
friend_name = input("Enter his friend's name: ")
verb = input("Enter a verb: ")
animal = input("Enter an animal: ")
adjective = input("Enter an adjective: ")
food = input("Enter a food item: ")

# Here is the Story template
story = f"""
Once upon a time, {human_name}  went to {place} very first time in his life. 
There, he/she saw a {adjective} {animal} and his own childhood friend {friend_name} he was {verb} happily with his {animal}. 
{human_name} was Surprised, he/she ran to {friend_name} decided to feed him and his {animal} some {food}. 
{friend_name} impressed with his kindness and said "Wow! You are so kind, {human_name}!"
{human_name} was so happy to hear that and said "Thank you, {friend_name}! I love to share my favourate things with my friends and I am glad to see you after a longtime!" .
After that, {human_name} and {friend_name} became best friends forever!
"""

# Display the final story
print("\nYour Mad Libs story:\n")
print("\n**********************\n")    
print(story)