import random

# Step 1 --> to make the computer to choose a random number in a predefined range of numbers
    # Specify a range of numbers to use
    # Specify to choose random number

    # Variables for step 1:
        # numbers_range = specifying the range to use
        # We don't need any range of numbers beforehand because random function itself can take range of numbers
        # computer_number = chosen number by the computer from the range (This is also the answer)

while True:
    try:
        numbers_range = int(input("Enter the largest number which is considered for the range"
                                  "(greater than 1 at least): \n"
                                  "Try to have a greater range to make it more fun \n"))
        computer_number = random.randint(1, numbers_range)
        break
    except ValueError:
        pass

# Step 2 --> Ask the user to enter a guessed number between that range
    # Tell the user what is the range of numbers to consider
    # tell the user to guess between those numbers
    # tell them if they have limited number of trials

    # variables for step 2:
        # user_number = to store the user guessed number

print("Try to guess the number that I have chosen between 0 and {}".format(numbers_range))
print("You only have 3 chances to guess")

chances = 5
number_of_guesses = 0

while True:

    try:
        user_input = int(input())
        number_of_guesses += 1
        if number_of_guesses == chances:
            break

        if user_input < computer_number:
            print("Guess higher")

        elif user_input > computer_number:
            print("Guess lower")

        else:
            print("got it")
            break

    except ValueError:
        print("No room to play other games ;)")

if user_input == computer_number:
    print("you got it in {} guesses".format(number_of_guesses))
else:
    print("you could not guess it right")
