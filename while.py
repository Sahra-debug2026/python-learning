import random
number = random.randint(1,10)

count = 1
guess = int(input('what is your guess?'))

while guess != number:
   
    count+=1
    guess = int(input('what is your guess?'))
print(f"After {count} times, your guess is {guess} and congratulations.")    