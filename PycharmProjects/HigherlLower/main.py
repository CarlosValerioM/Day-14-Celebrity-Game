#!/usr/bin/env python3
"""
celebrityGame.py - A game to guess which celebrity has more Instagram followers.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/17
License: MIT
Dependencies: data.py (contains the list of celebrities)

Description:
This script selects two random celebrities and asks the player to guess which one has more Instagram followers.
The player continues guessing until they make a mistake. Each correct guess increases their score.

Game Flow:
1. Two random celebrities are selected.
2. The player is presented with their name, profession, and country.
3. The player must choose which celebrity has more followers.
4. If the guess is correct, the score increases and a new round starts.
5. If the guess is incorrect, the game ends, displaying the final score.

Usage:
Run the script and follow the prompts:
    python celebrityGame.py

Example Output:
    Cristiano Ronaldo is a Footballer from Portugal.
    Taylor Swift is a Singer from the USA.
    Who has more followers? Type A or B: a
    Correct! Your score is 1.

    Kylie Jenner is a Model from the USA.
    Lionel Messi is a Footballer from Argentina.
    Who has more followers? Type A or B: b
    Sorry! You lose! Your score is 1.
"""
import random
from data import celebrities  # Import the list of celebrities from the data module

def main():
    """Main function that runs the celebrity follower comparison game."""

    game_active = True  # Controls the game loop
    score = 0  # Tracks the player's score

    while game_active:
        # Select two random celebrities from the dataset
        celeb1 = random.choice(celebrities)
        celeb2 = random.choice(celebrities)

        # Ensure that the two celebrities are not the same
        while celeb1 == celeb2:
            celeb2 = random.choice(celebrities)

        # Display celebrity information
        print(f"{celeb1['name']} is a {celeb1['profession']} from {celeb1['country']}.")
        print(f"{celeb2['name']} is a {celeb2['profession']} from {celeb2['country']}.")

        # Ask the user to choose who has more followers
        option = input("Who has more followers? Type A or B: ").strip().lower()

        # Determine the correct answer
        correct_choice = "a" if celeb1["followers"] > celeb2["followers"] else "b"

        if option == correct_choice:
            # Increase the score if the answer is correct
            score += 1
            print(f"\nCorrect! Your score is {score}\n")
        else:
            # End the game if the answer is incorrect
            game_active = False
            print(f"\nSorry! You lose! Your final score is {score}\n")


if __name__ == '__main__':
    main()