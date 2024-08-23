import random

# Milestone #1

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    # Generate random numbers between 1 and 100
   
    computer_number = random.randint(1, 100)
    player_number = random.randint(1, 100)
    
    # Print out the numbers (for testing purposes)
    print(f"The computer's number is {computer_number}")
    print(f"Your number is {player_number}")

# Run the game
high_low_game()


import random

# Milestone #2
def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    computer_number = random.randint(1, 100)
    player_number = random.randint(1, 100)
    
    print(f"Your number is {player_number}")
    user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

    # For testing purposes, we'll print the computer's number as well
    print(f"The computer's number is {computer_number}")

# Run the game
high_low_game()


import random

# Milestone #2
def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    computer_number = random.randint(1, 100)
    player_number = random.randint(1, 100)
    
    print(f"Your number is {player_number}")
    user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

    # For testing purposes, we'll print the computer's number as well
    print(f"The computer's number is {computer_number}")

# Run the game
high_low_game()


import random

# Milestone #3
def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    computer_number = random.randint(1, 100)
    player_number = random.randint(1, 100)
    
    print(f"Your number is {player_number}")
    user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    
    if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
        print("You were right!")
    else:
        print("Aww, that's incorrect.")
    
    # Reveal the computer's number
    print(f"The computer's number was {computer_number}")

# Run the game
high_low_game()
high_low_game



import random

NUM_ROUNDS = 5  # You can set the number of rounds here

# Milestone #4
def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
            print("You were right!")
        else:
            print("Aww, that's incorrect.")
        
        print(f"The computer's number was {computer_number}")
        print("")  # Add a blank line to separate rounds

# Run the game
high_low_game()


import random

NUM_ROUNDS = 5

# Milestone #5
def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Initialize the score
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
            print("You were right!")
            score += 1  # Increase score if the player is correct
        else:
            print("Aww, that's incorrect.")
        
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}")
        print("")  # Add a blank line to separate rounds
    
    print("Thanks for playing!")

# Run the game
high_low_game()


import random

NUM_ROUNDS = 5

# Extension #1
def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        
        # Safeguard input
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
            if user_guess in ["higher", "lower"]:
                break
            print("Invalid input! Please enter 'higher' or 'lower'.")
        
        if (user_guess == "higher" and player_number > computer_number) or (user_guess == "lower" and player_number < computer_number):
            print("You were right!")
            score += 1
        else:
            print("Aww, that's incorrect.")
        
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}")
        print("")  # Add a blank line to separate rounds
    
    print("Thanks for playing!")

# Run the game
high_low_game()

