# Assignment: HW 4
# File: DecisionTree.py
# Student: Todd Sakai
# UT EID: tfs523
# Course: C S 303E
# 
# Date: 9.21.25
# Description of Program: This program uses a decision tree to determine if a person will buy a computer based on their age, income, student status, and credit rating.

def main():
    age = int(input("Please enter person's age: "))
    income = input("Person's income (High, Medium, Low): ")
    is_student = input("Is this person a student (Yes or No)? ")
    credit = input("Does this person have good credit (Yes or No)? ")

    buys_computer = False

    if age >= 31 and age <= 40:
        buys_computer = True
    elif age > 40:
        if credit == 'No': 
            buys_computer = True
        else: 
            buys_computer = False
    else: 
        if is_student == 'Yes':
            buys_computer = True
        else:
            buys_computer = False

    if buys_computer:
        print("\nThis person will purchase a computer.")
    else:
        print("\nThis person will not purchase a computer.")
