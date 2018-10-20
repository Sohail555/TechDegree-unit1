import random

random_number = int(random.randint(1, 10))

def attempt():
   print("You are correct, it took you {} attempts".format(attempt_count))

def start_game():
    print("Welcome to the Guessing Game!")
    name = input("Can I take your name challenger ")
    print(name, "You have to guess the correct number in the fewest attempts")
    print(name, "Are you ready!")
    print("HINT: The number is between 1 - 10")


if __name__ == '__main__':
    start_game()

guess = 0
attempt_count = 0
while guess != random_number:
    try:
        guess = int(input("New number: "))
    except ValueError:
        print("Please enter a number")
        continue
    if guess > 10 or guess < 1:
        print("The number selected is outside the range")
        print("Plese select the number between 1 - 10")

    if random_number > guess:
        print("The number is higher")



    if random_number < guess:
        print("The number is lower")


    attempt_count += 1



attempt()