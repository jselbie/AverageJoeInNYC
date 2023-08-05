import random
Guessed = False
RandomNumber = random.randint(1, 1000000)
print(RandomNumber)
print("Guess The Number 1 to 1,000,000")
while Guessed == False:
    GuessedNumber = int(input(""))
    if int(GuessedNumber) == RandomNumber:
        print("Correct")
        Guessed = True
    elif GuessedNumber > RandomNumber:
        print("Lower")
    else:
        print("Higher")
