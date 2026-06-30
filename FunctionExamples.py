# Assignment: HW 6
# File: FunctionExamples.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: C S 303E
# 
# Date Created: 10/3/25
# Description of Program: Practice writing a variety of functions.

import math

#----------------------------------------------------------------------
# 1. Write a function to return the sum of three numbers.  I did this
#    one for you.

def sum3Numbers (x, y, z):
    """Return the sum of the three parameters."""
    return x + y + z

#----------------------------------------------------------------------
# 2. Write a function to return the product of three numbers.

def multiply3Numbers( x, y, z ):
    """Return the product of three perameters."""
    return x*y*z

#----------------------------------------------------------------------
# 3. Write a function to return the sum of up to 3 numbers.  It should
#    accept 1, 2, or 3 parameters.  Hint: any parameter not given
#    defaults to 0.

def sumUpTo3Numbers (x, y = 0, z = 0):
    """Returns the sum of numbers up to 3 numbers."""
    return x+y+z

#----------------------------------------------------------------------
# 4. Write a function to return the product of up to 3 numbers.  It
#    should accept 1, 2, or 3 parameters.  Hint: what should the
#    default be in this case?

def multiplyUpTo3Numbers (x, y = 1, z = 1 ):  # supply default args
    """Returns the product of up to 3 numbers."""
    return x*y*z
#----------------------------------------------------------------------
# 5. Write a function that takes 2 numbers as input and prints them
#    out in ascending order.  Make sure it works if they are equal.
#    Don't use lists or the sort function.

def printInOrder( x, y ):
    """Prints 2 input numbers in ascending order."""
    if(x < y):
        print(x,y)
    else:
        print(y,x)
#----------------------------------------------------------------------
# 6. Write a function that returns the area of a square, given the length 
#    of a side. Print an error message if side is negative. 

def areaOfSquare( side ):
    """Returns the area of a square, given the length of a side."""
    if (side < 0):
        return "Negative value entered"
    else:
        return side**2
#----------------------------------------------------------------------
# 7. Write a function that returns the perimeter of a regular 2D
#    figure of k sides, given the length of a side.  (Regular means all k
#    sides are the same length.)  Print an error message if side or k is
#    negative.

def perimeterOfFigure( k, side ):
    """Returns the perimeter of a shape with k sides given the length of one\
        of the sides."""
    if (k < 0 or side < 0):
        return "Negative value entered"
    else:
        return k*side

#----------------------------------------------------------------------
# 8. Write a function that returns the length of the diagonal of a
#    rectangle of given height and width.  This is computed as the square
#    root of the sum of the squares of h and w.

def diagonalOfRectangle( h, w ):
    """Returns the length from corner to corner of a rectangle given the\
        height and width."""
    if (h < 0 or w < 0):
        return "Negative value entered"
    else:
        return math.sqrt(h**2+w**2)

#----------------------------------------------------------------------
# 9. Write a function that returns the area of a circle, given the
#    radius.  Use math.pi. Print an error message if radius is negative.

def areaOfCircle( radius ):
    """Returns the area of a circle given the radius."""
    if (radius < 0):
        return "Negative value entered"
    else:
        return math.pi*radius**2

#----------------------------------------------------------------------
# 10. Write a function that returns the circumference of a circle given
#    the radius.  Use math.pi. Print an error if radius is negative.

def circumferenceOfCircle( radius ):
    """Returns the circumference of a circle given the radius."""
    if (radius < 0):
        return "Negative value entered"
    else:
        return 2*math.pi*radius

#----------------------------------------------------------------------
# 11. Write a function: given parameters d1, d2, x, returns whether
#    both d1 and d2 are both factors of (evenly divide) x.  You can
#    assume all values are integers.

def bothFactors( d1, d2, x ):
    """Given (d1, d2, x), return whether or not d1 AND d2 evenly divide x"""
    if ((x%d2)==0) and ((x%d1)==0):
        return "True"
    else:
        return "False"

#----------------------------------------------------------------------
# 12. Given a value x, compute and print out the area and circumference of a circle with
#    radius x and the area and perimeter of a square with side x.  Call your previous 
#    functions for these computations.  Leave a blank line above and below the printing.

def squareAndCircle( x ):
    """Given a value x, it prints out the area and circumference of a circle with radius x\
        as well as the area an perimeter of a square with side x."""
    if (x < 0):
        return "Negative value entered"
    print()
    print("Circle with radius", x, "has:")
    print("\tArea: ",areaOfCircle(x))
    print("\tCircumference: ",circumferenceOfCircle(x))
    print("Square with side", x, "has: ")
    print("\tArea: ",areaOfSquare(x))
    print("\tCircumference: ",perimeterOfFigure(4,x))
    print()

#----------------------------------------------------------------------
# 13. Write a function that returns the factorial of a positive
#     integer n.  Use a for loop to compute the factorial.  You can
#     assume the input is an integer, but print an error message if
#     it's not positive and return None.

def factorial( n ):
    """Returns the factorial of a positive integer n."""
    if n < 0:
        return "Input must be positive"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#----------------------------------------------------------------------
# 14. Write a function that returns the number of digits in the
#     decimal representation of an integer n.  You can assume that
#     n is positive.  E.g., numberLength( 12345 ) = 5.  Don't convert
#     the argument to a string. 

def numberLength( n ):
    """Return the number of digits in the decimal representation of a positive integer n."""
    count = 0
    temp_n = n
    while temp_n > 0:
        temp_n //= 10
        count += 1
    return count

#----------------------------------------------------------------------
# 15. Write a function that sums positive numbers entered by the user
#     and returns the sum.  You can assume that user inputs are
#     numbers (float or int).  If the number entered is negative, print 
#     an error message and continue;  don't add it to the sum.  There 
#     can be any number of inputs.  Stop when the user enters 0. 
#     (Note: This was a problem from Exam1 in an earlier semester.)

def sumPositiveNumbers():
    """Sums positive numbers entered by the user and returns the sum. \
    Stops when the user enters 0."""
    total = 0
    while True:
        num_str = input("Enter a number: ")
        num = float(num_str)
        if num == 0:
            break
        if num > 0:
            total += num
        else:
            print("Illegal input.")
    return total

#----------------------------------------------------------------------
# 16. Complete the function below that sums the following series:
# 
#      (1 * 2) + (2 * 3) + (3 * 4) + ... + (n-1 * n)
# 
#    Your function should use a for loop to compute the answer. Return,
#    don't print, the answer.  You can assume that n is a positive integer
#    greater than 1.  For example if n is 4, this is the series (1 * 2) +
#    (2 * 3) + (3 * 4) and your function should return 20.

def sumSeries( n ):
    """Sums the series (1 * 2) + (2 * 3) + ... + (n-1 * n) and returns the sum."""
    total=0
    for i in range(1,n):
        total += i*(i+1)
    return total

sumPositiveNumbers()