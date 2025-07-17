import random


top_of_range = input("Type a number between 1 and 100: ")
""" i am taking the input from the user"""

if top_of_range.isdigit():
    """isdight->if the user return a number then it is true other wise fulse"""
    top_of_range = int(top_of_range)
    """previously top_of_range is a string that string will covert it into the integer"""

    if top_of_range <= 0 :
        print("please type a number larger than 0 next time")
        quit()
else:
    print("please type a number next time")
    quit()

random_number = random.randint(0,top_of_range)
"""print(random_number)"""

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("you guessed right")
        break
    elif user_guess < random_number:
        print("your guess is too low")
    else:
        print("your guess is too high")

print("you guessed in", guesses,"time")
