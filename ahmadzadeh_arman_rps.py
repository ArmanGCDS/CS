#cat                                                                                                                                              
import random                                                                          #Enable random generation                                                                         
                                                                                                  

def rock():                                                                            #Function for rock display message              
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
def paper():                                                                           #Function for paper display message
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
def scissors():                                                                        #Function for scissors display message 
    print("""                                                                           
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
def rps_winner(player1_choice, player2_choice):                                          #Function for deciding rps winner (player 1’s choice and player 2’s choice)
                                                                                         # retuns 1 for player1 winning, 2 for second player winning and 0 for a tie
    
    if player1_choice == "rock":                                                         #If player 1 choses rock
        rock()                                                                           #Call rock function
        if player2_choice == "scissors":                                                 #if player 2 choses scissors
            scissors()                                                                   #Call scissors function
            winner = 1                                                                   #The winner is player 1
        elif player2_choice == "paper":                                                  #Then if player 2 choses paper
            paper()                                                                      #Call paper function
            winner = 2                                                                   #The winner is player 2
        else:                                                                            #If anything else
            rock()                                                                       #Call rock function
            winner = 0                                                                   #The winner is 0
    elif player1_choice == "scissors":                                                   #Then if player 1 choses scissors
        scissors()                                                                       #Call scissors function
        if player2_choice == "paper":                                                    #if player 2 choses paper
            paper()                                                                      #Call paper function
            winner = 1                                                                   #The winner is player 1
        elif player2_choice == "rock":                                                   #Then if player 2 choses rock
            rock()                                                                       #Call rock function
            winner = 2                                                                   #The winner is player 2
        else:                                                                            #If anything else
            scissors()                                                                   #Call scissors function
            winner = 0                                                                   #The winner is 0
    else:                                                                                #Else player 1 choses anything else (paper)
        paper()                                                                          #Call paper function
        if player2_choice == "rock":                                                     #if player 2 choses rock
            rock()                                                                       #Call rock function
            winner = 1                                                                   #The winner is player 1
        elif player2_choice == "scissors":                                               #Then if player 2 choses scissors 
            scissors()                                                                   #Call scissors function
            winner = 2                                                                   #The winner is player 2
        else:                                                                            #If anything else
            paper()                                                                      #Call paper function
            winner = 0                                                                   #The winner is 0
                
    return winner                                                                        #Return the information of who is the winner (0, 1, or 2)
     

def get_machine_choice(valid_weapons, game_mode):                                       #This function returns a weapon based on the game mode, 
                                                                                        #if the game mode is random is returns a random weapon otherwise,
                                                                                        # first creates a random pattern and then it follows the pattern
    global machine_pattern                                                              # creates a global variable machine pattern
    if game_mode == 'random':                                                           # check if game mode is random
        return random.choice(valid_weapons)                                             # retuns a random choise from list of weapons
    elif game_counter == 0:                                                             # is this the first time playing and the game mode is not random?
        machine_pattern = create_random_pattern(valid_weapons)                          # Create a random pattern
        return machine_pattern[0]                                                       # return the fist weapon in the random pattern
    else:                                                                               # game mode is pattern and played before
        return machine_pattern[game_counter % len(machine_pattern)]                     # return a choise from the pattern


def create_random_pattern(valid_weapons):                                               #This function creates a random pattern from the list of valid weapons

    n = random.choice([1, 2, 3, 4, 5])                                                  # length of random pattern is capped to 5
    pattern = []                                                                        # create an empty list of pattern
    while len(pattern) < n:                                                             # repeat while length of the pattern is less than n
        pattern.append(random.choice(valid_weapons))
    #print('random pattern is:', pattern)                                               # for testing if the code follows the pattern
    return pattern                                                                      # return the chosen pattern


def rps(valid_weapons, game_mode):                                                       #Function for deciding the weapons

    player_choice = input("Select your weapon out of rock, paper or scissors: ")         #The players’ choice is the input “select your weapon out of rock, paper or scissors”    
    while not any(player_choice.lower() == word for word in valid_weapons):              #When the is no word from the valid weapons list in the user’s response (upper or lower case do not matter) 
        print(player_choice, "is not valid, Please select a valid weapon.")              #Display the message “players choice is an nvalid response, please select a valid weapon”
        player_choice = input("Select your weapon out of rock, paper or scissors: ")     #The players’ choice is the input “select your weapon out of rock, paper or scissors”
         
    machine_choice = get_machine_choice(valid_weapons, game_mode)                        #Gets the machine choise from the get_machine_choice function
    print("My weapon is:", machine_choice)                                               #Display the message “My weapon is: the machine choice”
    winner = rps_winner(player_choice.lower(), machine_choice)                           #The winner = winner (player choice lower or upper case, machine’s choice    
    return winner                                                                        #Return the winner to the code

if __name__ == "__main__":                                                               #start of the program

    global game_counter                                                                  #seting up global variable visable in all functions
    game_counter = 0                                                                     #counter that keeps track of the game count to be used in a fixed pattern game
    score = 0                                                                            #Score variable is set to 0
    get_game_mode = input("Do you want to make the game more intresting by discovering a machine pattern? You can always win! (y/n):")
    valid_weapons = ["rock", "paper","scissors",]                                        #The valid weapons are in the list (rock, paper, scissors)

    if get_game_mode.lower() == 'y':                                                     #Checking for the user's game mode choice
        game_mode = 'pattern'                                                            # game mode is "pattern"
        machine_pattern = create_random_pattern(valid_weapons)                           # create a random pattern
    else:
        game_mode = 'random'                                                             #game mode is random, i.e no pattern

    while True:                                                                          #While true forever loop
        winner = rps(valid_weapons, game_mode)                                           #The_winner is from rps function
        game_counter += 1
        if winner == 1:                                                                  #If the winner is 1
            print('Congratulation, you WON!')                                                #Display message, “Congratulations, you WON!”
            score += 1                                                                       #Score variable is increase by 1
            print("Score:", score)                                                           #Display score
        elif winner == 2:                                                                 #Then if the winner is 2
            print('Machine WINS!, try again, maybe next time')                            #Display message “Machine WINS!, try again, maybe next time”
            score -= 1                                                                    #Score variable is decreased by 1
            print("Score:", score)                                                        #Display score
        else:                                                                             #If anything else
            print('You draw against the machine!')                                        #Display message “You have drawn against the machine!”
            score = score                                                                 #score is not changed
            print("Score:", score)                                                        #Display score
        
        if input("Want to play again? (y/n): ").lower() != "y":                           #If the input “Want to play again?, yes or no” Lower or upper case, does not equal yes:         
                print("goodbye. your total score against machine is, ", score)            #Display message “goodbye”
                break                                                                     #Exit while true loop and end code