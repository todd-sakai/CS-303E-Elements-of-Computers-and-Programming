# Assignment: HW5
# File: LuckySevens.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: CS303E
# 
# Date: 9/30/25
# Description of Program: The user gambles a starting stake by repeatedly rolling two dice, winning $4 on a sum of 7 and losing $1 on any other sum, until their money is gone. You can play until you don't want to anymore

def main():
    import random
    maxStake=0
    roll=1
    while(roll==1):
        currentStake=input("How many dollars would you like to gamble? ")

        while(currentStake.isdigit()==False):
            print("Answer must be a positive integer (dollars to gamble).  Try again!")
            currentStake=input("How many dollars would you like to gamble? ")
        currentStake=int(currentStake)
        print(f"You've said you're going to gamble ${currentStake}. Good luck!")

        while(currentStake>0):
            if(currentStake>maxStake):
                maxStake=currentStake
            diceOne=random.randint(1,6)
            diceTwo=random.randint(1,6)
            diceSum=diceOne+diceTwo
            print(f"{roll}: rolled ({diceOne}, {diceTwo}), sum = {diceSum}")
            
            if(diceSum!=7):
                roll+=1
                currentStake-=1
                print(f"Sorry, you lost $1. Better luck next time! Your stake is ${currentStake}")

            elif(diceSum==7):
                roll+=1
                currentStake+=4
                print(f"Congratulations, you win $4! Your stake is ${currentStake}")

        print()
        print(f"You're out of money after {roll-1} rolls.")
        print(f"Your highest stake was: ${maxStake}")
        print()
        again=input("Would you like to play again (yes or no)? ")
        if(again=="no"):
            print("Thanks for playing!")
            roll=0
        else:
            roll=1
            maxStake=0
    
main()