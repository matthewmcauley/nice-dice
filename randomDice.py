import random

print("\n\n\n")
print("Welcome to the Dice Game")

sideDice = input("How many sides should the dice have? ")
numRolls = input("And how many times would you like to roll? ")

print("Rolling a " + str(sideDice) + " sided dice, " + str(numRolls) + " times.")
print("Here we go...")

sumRolls = 0

for num in range (1,numRolls+1):
    rolled = random.randint(1,sideDice)
    sumRolls+=rolled
    print("Roll " + str(num) + ": " + str(rolled))

print("You rolled a " + str(sumRolls))
print("\n\n\n")
