import random

def start_game():
   random_number = int(random.randint(1, 10))
   print("Welcome to the Guessing Game!")
   name = input(" Can I take your name challenger ")
   print(name, "You have to guess the correct number in the fewest attempts")
   print(name, "Are you ready!")


def _game()
guess = 0

attempt_count = 1
while guess != randon_number:
    guess = int(input("New number: "))
    if random_number > guess:
        print("The number is lower")
        continue
    attempt_count += 1
    elif random_number < guess:
        print("The number is higher")
        continue
    attempt_count += 1

print("You are correct")
print("test")