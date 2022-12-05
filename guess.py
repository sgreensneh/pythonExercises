import random

number_to_be_guessed = random.randint(1,100)
guess = int(input("Guess a number 1-100: "))
number_to_be_guessed = 1

while number_to_be_guessed < 3:

    if guess == number_to_be_guessed:
        print("you got it right")
        break

    else:
        guess = int(input("Guess a number between 1-100: "))
    number_to_be_guessed  += 1

    if number_to_be_guessed == 3:
        print("Try again later, it's unfortunate you could not guess", number_to_be_guessed)



