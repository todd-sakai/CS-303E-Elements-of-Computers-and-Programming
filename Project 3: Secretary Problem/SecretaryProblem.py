# Assignment: Project 3
# File: SecretaryProblem.py
# Student: Todd Sakai
# UT EID: tfs523
# Course: C S 303E
# 
# Date: 12.1.25
# Description of Program: This program simulates the Secretary Problem by running experiments on applicant data to test the optimal stopping strategy.

# Imports
import random
import math
import os

# Function definitions
def createDataFile(numberOfLines, fileName):
    """This creates a file of lines of data for the Secretary
    Problem. Each line contains between 25 and 100 data points, each a
    float between 0 and 100.  The idea is that these are the rankings
    of secretaries.  In the file each ranking has 3 digits of
    precision.  I originally made the rankings integers, but this led
    too often to duplicate rankings.  It's still possible, but
    unlikely, that two rankings could be identical.

    """
    # Open a new file for writing.  If a file of this name exists,
    # this will overwrite it.
    outfile = open(fileName, "w")
    
    # We want to generate a file with numberOfLines lines of data
    for i in range(numberOfLines):

        # Each line has a random number of data points between 25 and
        # 100.  This is the number of candidates in that experiment.
        lineLen = random.randint(25, 100)

        # This is a list of the data items, each a random float
        # between 0 and 100. These are the rankings of the
        # secretaries. It's unlikely that any two data points will be
        # identical, though that's possible.
        data = [ (random.random() * 100) for j in range(lineLen) ]
        
        for datum in data:
            # Write each datum to the file with 3 digits of precision
            # followed by a blank.  All data from an experiment will
            # be on one line.
            outfile.write( format( datum, ".3f" ) + " " )

        # Close out the line (experiment) by writing a newline.
        outfile.write( "\n" )
            
    # Close the output file.
    outfile.close()

def readDataFile(fileName):
    data = []
    infile = open(fileName, "r")

    for line in infile:
        ranks = [float(x) for x in line.split()]
        data.append(ranks)
    infile.close()
    
    return data 

def chooseSecretary(ranks):
    k = round((len(ranks) / math.e))
    benchmark = max(ranks[:k])

    for i in range(k, len(ranks)):
        if ranks[i] > benchmark:
            return i
    return -1

# Main function definition
def main():
    fileName = input("Enter data file name: ")
    
    if not os.path.isfile(fileName):
        print("File doesn't exist: ", fileName)
    else:
        data = readDataFile(fileName)

        totalInterviews = len(data)
        noChoiceCount = 0
        bestChoiceCount = 0
        badChoiceCount = 0

        for ranks in data:
            choiceIndex = chooseSecretary(ranks)

            if choiceIndex == -1:
                noChoiceCount += 1
            else:
                choiceScore = ranks[choiceIndex]
                bestScore = max(ranks)
                if choiceScore == bestScore:
                    bestChoiceCount += 1
                else:
                    badChoiceCount += 1

        s1 = format(noChoiceCount / totalInterviews * 100, ".2f") + "%"
        s2 = format(bestChoiceCount / totalInterviews * 100, ".2f") + "%"
        s3 = format(badChoiceCount / totalInterviews * 100, ".2f") + "%"

        print("Results:")
        print("  No choice made:  ", s1)
        print("  Best choice made:", s2)
        print("  Bad choice made: ", s3)

# Call to main function
main()