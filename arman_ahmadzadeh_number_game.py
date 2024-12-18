import random

name = input("What is your name?").lower()
print('good luck,', name)
correct = 0
rounds = 0

while True:
    number = random.randint(1, 10)
    guesses = 5

    while guesses > 0:
        guess = input("Guess that number:").lower()

        try:
            guess = int(guess)

            if guess >= 1 and guess <= 10:
                pass
            else:
                print("Please enter a number between 1 and 10!")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if guess == number: 
            print("You got it!")
            correct += 1 
            break 
        elif guess > number:
            print("Your number is too high")
        else: 
            print("Your number is too low")
        guesses -= 1

    if guesses == 0:
        print("You lost this round")
    
    rounds += 1 

    while True:
        play_again = input(f"You had {guesses} remaining and currently have {correct} correct out of {rounds}. Would you like to play again? Enter y or n: ")
        
        if play_again == "n":
            exit()
        elif play_again == "y":
            break
        else: 
            print('Invalid response, limit to y or n')
    