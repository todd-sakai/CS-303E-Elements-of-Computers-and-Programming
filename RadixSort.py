# Assignment: HW10
# File: RadixSort.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: CS303E
# 
# Date: 11.3.25
# Description of Program: A program that sorts a list of randomly generated numbers using the Radix sorting method

# Imports
import random

# Global constants
ROUNDS_OF_SORTING = 3
NUMBER_OF_DATA_POINTS = 50
TEST_DATA = [ random.randint(0, 999) for i in range(NUMBER_OF_DATA_POINTS) ]

# Function definitions
def listOfDigits( num ):
    # Given a non-negative integer num, return a list of its digits,
    # from least to most significant.
    if num == 0:
        return [0]
    
    digits = []

    while num > 0:
        digits.append(num % 10)
        num //= 10

    return digits

def getDigit( num, k ):
    # Given a list of digits, select the kth one, if any.  Otherwise,
    # return 0.
    digits = listOfDigits(num)
    if k in range(len(digits)):
        return digits[k]
    else:
        return 0

# Main function definition
def radixSort( testData, rounds ):
    # Given a list testData of random integers, none of more than rounds
    # digits, use radix sort to sort them.
    print( "\nInput data:" )
    print( testData )

    for i in range(rounds):
        sortLists = [ [] for j in range(10) ]

        for number in testData:
            digit = getDigit(number, i)
            sortLists[digit].append(number)
        
        flattened_list = []
        for sublist in sortLists:
            for number in sublist:
                flattened_list.append(number)
        testData = flattened_list
    
    finalSortedData = testData

    print( "\nFinal sorted list:" )
    print( finalSortedData )

# Call to the main function
radixSort( TEST_DATA, ROUNDS_OF_SORTING )