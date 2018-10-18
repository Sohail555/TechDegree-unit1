import random

random_number = int(random.randint(1, 10))
GAMER_NAME = ""

def attempt():
    if attempt_count == 1:
        print("You are correct, it took you 1 attempt.")
    else:
        print("You are correct, it took you {} attempts".format(attempt_count + 1))


def start_game():
    print("Welcome to the Guessing Game!")
    GAMER_NAME = input("Can I take your name challenger ")
    print(GAMER_NAME,"You have to guess the correct number in the fewest attempts")
    print(GAMER_NAME, "Are you ready!")
    print("HINT: The number is between 1 - 10")


def scope():
    if guess > int(10): # Greater than 10
        print("Please select a number between 1 - 10")
    if guess < int(1): # Less than 1
        print("Please select a number between 1 - 10")

def new_scope():
    # if the guess is less than 10 or if its greater than 1
    # return a True
    if guess < 10 or guess > 1:
        return True
    else:
        # if its not less than 10 or greater than 1, return False
        return False




start_game()

guess = 0
attempt_count = 0
while guess != random_number:
    try:
        guess = int(input("New number: "))
    except ValueError:
        print("Please enter a number")
        continue

    if new_scope(): # if scope() returns True

        print("Please select a number between 1 - 10")
        if random_number > guess: # check their guess against random_number
            print("The number is higher")
            attempt_count += 1
            continue

        if random_number < guess:
            print("The number is lower")
            attempt_count += 1
            continue

    else: # if scope() returns False
        print("Oops not within range.")
        print("Please select a number between 1 - 10")
        continue

    attempt()

    play_again = input("Do you want to play again(Yes/No)")
    if play_again.lower() == "yes":
        while guess != random_number:
            try:
                guess = int(input("New number: "))
            except ValueError:
                print("Please enter a number")
                continue

            if new_scope(): # if scope() returns True

                print("Please select a number between 1 - 10")
                if random_number > guess: # check their guess against random_number
                    print("The number is higher")
                    attempt_count += 1
                    continue

                if random_number < guess:
                    print("The number is lower")
                    attempt_count += 1
                    continue

            else: # if scope() returns False
                print("Oops not within range.")
                print("Please select a number between 1 - 10")
                continue
        attempt()
    print("Thanks for playing")


#if __name__ == '__main__':
    start_game()