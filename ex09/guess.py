from ast import Num
from pickle import TRUE
import sys
import random

print("\nThis is an interactiv guessing game!\n"
       "You have to enter a umber between 1 and 99 to find out the secret number.\n"
       "Type 'exit' to end the game.\n")
num = 42
#num = random.randint(1, 99)
print(num)
tries = 0
while TRUE:
    print("What's your guess between 1 and 99?")
    guess = int(input(">>"))
    tries += 1
    if guess == num:
        if guess == 42 and num == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if tries == 1:
            print("Congratulations.You got it on your first try!")
            exit()
        print("Congratulations,you've got it!")
        print(f"You won in {tries}")
        exit()
    elif guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")
    