# File: RecursiveFunctions.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: CS303E
# 
# Date: 11.21.25
# Description of Program: This program is meant to help me build proficiency in writing recursive functions

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList(key, L[1:])
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Return the sum of the non-negative integers to n.
   E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5 """
   if n == 0:
        return 0
   else:
        return n + addToN(n - 1)

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. 
   E.g., findSumOfDigits( 1234 ) = 10 """
   if n < 10:
        return n
   else:
        return (n % 10) + findSumOfDigits(n // 10)

def integerToBinary( n ):
   """ Given a nonnegative integer n, return the 
   binary representation as a string. E.g., 
   integerToBinary( 10 ) = '1010' """
   if n < 2:
      return str(n)
   else:
      return integerToBinary(n // 2) + str(n % 2)

def integerToList( n ):
   """ Given a nonnegative integer, return a list of the 
   digits (as strings). 
   E.g., integerToList( 123 ) = ['1', '2', '3'] """
   if n < 10:
       return [str(n)]
   else:
       return integerToList(n // 10) + [str(n % 10)]

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome.
   Case counts: 'abA' is not a palindrome. """
   if len(s) <= 1:
       return True
   else:
       return s[0] == s[-1] and isPalindrome(s[1:-1])


def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if not s:
       return None
   elif s[0].isupper():
       return s[0]
   else:
       return findFirstUppercase(s[1:])

# for this one, don't reverse the string.
def findLastUppercase( s ):
   """ Return the last uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if not s:
       return None
   else:
       res = findLastUppercase(s[1:])
       if res is not None:
           return res
       elif s[0].isupper():
           return s[0]
       else:
           return None

def negateItems( lst ):
   """Assume lst is a list of numbers.  Return a list
   of the negations of those numbers."""
   if not lst:
       return []
   else:
       return [-lst[0]] + negateItems(lst[1:])

def findLargest( lst ):
   """Assume lst is a list of numbers. Recursively find
   and return the largest element."""
   if not lst:
       return None
   elif len(lst) == 1:
       return lst[0]
   else:
       max_rest = findLargest(lst[1:])
       if lst[0] > max_rest:
           return lst[0]
       else:
           return max_rest

# I posted a short video on the class webpage explaining 
# helper functions.  If you're stuck on this one, view
# that video and see if it helps.

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the offset of the first uppercase letter;
   assume you are starting at index. Return -1 
   if there is none."""
   if not s:
       return -1
   elif s[0].isupper():
       return index
   else:
       return findFirstUppercaseIndexHelper(s[1:], index + 1)

# The following function is already completed for you. But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any. Return -1 if there is none. This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper(s, 0)