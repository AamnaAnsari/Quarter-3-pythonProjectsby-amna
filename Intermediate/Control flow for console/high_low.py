import random

def high_low_game(rounds):
    score = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")

        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print("Your number is:", your_number)

        guess = input("Is your number higher or lower than the computer's? (Type 'higher' or 'lower'): ").lower()

        # Determine if guess was correct
        if your_number > computer_number and guess == "higher":
            print("Correct! You got a point.")
            score += 1
        elif your_number < computer_number and guess == "lower":
            print("Correct! You got a point.")
            score += 1
        else:
            print("Wrong guess!")
        
        
    print(f"\nGame Over! Your total score: {score}/{rounds}")

# Run the game with desired number of rounds
rounds_to_play = int(input("How many rounds do you want to play? "))
high_low_game(rounds_to_play)
