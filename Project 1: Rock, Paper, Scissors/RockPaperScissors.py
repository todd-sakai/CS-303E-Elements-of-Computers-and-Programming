# Assignment: Project 1
# File: RockPaperScissors.py
# Student: Todd Sakai 
# UT EID: tfs523
# Course: C S 303E
# 
# Date: 10.09.25
# Description of Program: Play rock, paper, scissors against a robot!!

import random
import sys

# Symbolic constants
ROCK = '1'
PAPER = '2'
SCISSORS = '3' 
valid_plays = [ROCK, PAPER, SCISSORS]
WELCOME_MESSAGE = "Welcome to a game of Rock, Paper, Scissors!"
GOODBYE_MESSAGE = "Thanks for playing. Goodbye!"

# This is a global variable that indexes into the 'oracle' to select
# the next machine play.

machinePlayCounter = 0

def machinePlay ():
    """The machine chooses one of the three moves randomly,
    unless there's an oracle passed on the command line.  Then
    we choose machine plays in order from that."""
    global machinePlayCounter
    hasOracle = ( len( sys.argv ) > 1 )
    if hasOracle:
        machineOracle = sys.argv[1]
    if hasOracle and machinePlayCounter < len(machineOracle):
        play = machineOracle[ machinePlayCounter ]
        machinePlayCounter += 1
    else:
        # This assume you've defined ROCK = "1", etc.
        play = random.choice([ROCK, PAPER, SCISSORS])
    return play

def playName( play ):
    """For each possible move, return the name to print. For example, 
       ROCK prints as 'rock'."""
    if play == ROCK:
        return "rock"
    elif play == PAPER:
        return "paper"
    elif play == SCISSORS:
        return "scissors"

def defeats( play1, play2 ):
    """Boolean valued function that returns True iff play1 defeats
    play2."""
    return (play1 == ROCK and play2 == SCISSORS) or \
           (play1 == SCISSORS and play2 == PAPER) or \
           (play1 == PAPER and play2 == ROCK)

def printStats( plays, wins, losses, draws ):
    """Print the statistics for the sequence of games played."""
    if plays == 0:
        print("No games were completed.")
    else:
        print("Game statistics:")
        print("  Games played: " + str(plays))
        print("  You won:      {} ({:.1%})".format(wins, wins/plays))
        print("  You lost:     {} ({:.1%})".format(losses, losses/plays))
        print("  No winner:    {} ({:.1%})".format(draws, draws/plays))

# THE GAMMMEEEEEEEEE
def main():
    """Main function to run the Rock, Paper, Scissors game."""
    # Initialize counters
    games_played = 0
    user_wins = 0
    user_losses = 0
    draws = 0

    # Print welcome message
    print(WELCOME_MESSAGE)

    while True:
        print("\nChoose your play:")
        print("  Enter 1 for rock;")
        print("  Enter 2 for paper;")
        print("  Enter 3 for scissors;")
        print("  Enter 4 to exit: ", end="")
        
        # Get user's play
        user_play = input()

        # If user doesn't want to play anymore (A way out of while loop)
        if user_play == '4':
            break
        
        # Check if user's play is valid
        if user_play not in valid_plays:
            print("Illegal play entered. Try again!")
            continue

        # If a valid game is played
        games_played += 1
        opponent_play = machinePlay()
        
        # Print the game results
        print("You played " + str(playName(user_play)) + "; your opponent played " + str(playName(opponent_play)))
        if defeats(user_play, opponent_play):
            print("Congratulations, you won!")
            user_wins += 1
        elif defeats(opponent_play, user_play):
            print("Sorry, you lost!")
            user_losses += 1
        else:
            print("There's no winner. Try again!")
            draws += 1
            
    printStats(games_played, user_wins, user_losses, draws)
    print(GOODBYE_MESSAGE)
main()