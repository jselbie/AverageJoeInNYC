a = 6
b = 3
if a > b:
    print("A is greater than B")

x = 4
if x > 3:
    x += 2
print(x)

Has_Key = True
if Has_Key == True:
    print("Wow you have the key")

print(5>4)
print(10==10)
print(4>5 or 4>6)

player_age = 11
if player_age >= 18:
    print("If you smart you in college")
elif player_age >= 13:
    print("You is teenager")
elif player_age >= 7:
    print("You can go to iD tech thing")
else:
    print("You're practically a baby hahahahaha")

y = 3
if y > 2 and y < 4:
    print("y is equal to 3")

player_has_item = False
score = 50
won = False
if player_has_item and score > 100:
    won = True
if not won:
    print("You haven't beaten the game yet.")
elif won:
    print("You won the game!")

    import random

    computer_number = random.randrange(0, 101)

    guessed = False