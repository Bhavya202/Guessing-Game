# Number Guessing Game

import random
canPlay = True
print("!!Number Guessing Game!!")
print()

while canPlay :
    number = input("Enter A Number For An Upper Limit: ")

    if number.isdigit() :
        print("Let's Start")
        print()
        number = int(number)
        canPlay = False
    else :
        print("Try Again!")

randomNumber = random.randint(1, number)

guess = None
count = 5

while count != 0 :
    guess = input("Enter A Number Between 1 and " + str(number) + " : ")

    if guess.isdigit() :
        guess = int(guess)

    if guess == randomNumber :
        print("Congratulations!! You Got It.")
        break
    elif guess > randomNumber :
        print("Try Again! Think Backward.")
        count = count-1
    elif guess < randomNumber :
        print("Try Again! Think Forward.")
        count = count-1

if count == 0 :
    print("No Guess Left.")
    print("YOU LOST!!", "The Number is", randomNumber)