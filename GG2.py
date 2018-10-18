import random

random_number = int(random.randint(1, 10))

def attempt():
    if attempt_count == 1:
        print("You are correct, it took you 1 attempt.")
    else:
        print("You are correct, it took you {} attempts".format(attempt_count))

def start_game():
    print("Welcome to the Guessing Game!")
    name = input("Can I take your name challenger ")
    print(name, "You have to guess the correct number in the fewest attempts")
    print(name, "Are you ready!")
    print("HINT: The number is between 1 - 10")



start_game()
guess = 0
attempt_count = 0
while guess != random_number:
    try:
        guess = int(input("New number: "))
    except ValueError:
        print("Please enter a number")
        continue
    if random_number > guess:
        print("The number is higher")
        continue
    attempt_count += 1
    if random_number < guess:
        print("The number is lower")
        continue
    attempt_count += 1

attempt()