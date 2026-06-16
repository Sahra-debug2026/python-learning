import random
number=random.randint(1,10)

guess=int(input("what is your guess?")) 

if guess == number:
    print("Congratulations! You guessed it!")
else:
    print(f"sorry, try again. the number was {number}.")    