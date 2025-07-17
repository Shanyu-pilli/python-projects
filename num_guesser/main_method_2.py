import random

number_to_guess = random.randint(1,10)

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
        else:
            print('comgratulations! you guessed the number')
            break
    except ValueError:
        print("Invalid input")