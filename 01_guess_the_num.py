# Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. This will get you started with the random library if you haven't already used it.

# imports the random program
import random

random_number = random.randint(0,20)

while True: 
    user_guess = int(input("I am thinking of a number between 0 and 20. If you guess correctly, I shall allow you to pass. "))
    if user_guess < random_number:
        print("Your number is too low")
        continue
    elif user_guess > random_number:
        print("Your number is too high")
        continue
    elif user_guess == random_number:
        break
print("Good job! You guessed correctly! You may pass.")

user_guess != random_number