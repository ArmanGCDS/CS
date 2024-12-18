import random

def madlib():
    noun = input("Enter a noun")
    adjective = input("Enter an adjective")
    verb = input("Enter a verb")
    adverb = input("Enter a adverb")
    proper_noun = input("Enter a proper noun")
    place = input("Enter a place")
    preposition = input("Enter a preposition")

    print(f"A very {adjective} {noun} named {proper_noun} decided to {verb} {adverb} in the {place} {preposition}.")

def cointoss():
    heads = 0
    tails = 0
    tosses = 0

    coin_toss = (["heads", "tails"])
        
    for _ in range(5):
        results = random.choice(coin_toss)
        if results == "heads":
                heads += 1
                tosses += 1
        elif results == "tails":
                tails += 1
                tosses += 1
        print(results)
    print(heads, "= heads", tails, "= tails",tosses, "= tosses")

while True:

    game_choice = input(("Do you want to play madlib or coin toss? (m/c):")).lower()

    if game_choice == "m": 
        madlib()

    elif game_choice == "c":
        cointoss()

    if input("Want to play again? (y/n): ").lower() != "y":
        break