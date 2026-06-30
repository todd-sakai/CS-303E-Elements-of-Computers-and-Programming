# Assignment: HW9
# File: MyListFunctions.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: CS 303E
# 
# Date: 10.24.25
# Description of Program: A collection of functions to manipulate strings without using existing methods

def myAppend( lst, x ):
    # Return a new list that is like lst but with 
    # the element x at the right end
    return lst + [x]

def myExtend( lst1, lst2 ):
    # Return a new list that contains the elements of
    # lst1 followed by the elements of lst2 in the order
    # given
    return lst1 + lst2

def myMax( lst ):
    # Return the element with the highest value.
    # If lst is empty, print "Empty list: no max value"
    # and return None.  You can assume that the list
    # elements can be compared.
    if len(lst) == 0:
        print ("Empty list: no max value")
    else:
        output = lst[0]
        for element in lst:
            if element >= output:
                output = element
        return output

def mySum( lst ):
    # Return the sum of the elements in lst.  Assume
    # that the elements are numbers.
    output = 0
    for elementIndex in range(len(lst)):
        output += lst[elementIndex]
    return output

def myCount( lst, x ):
    # Return the number of times element x appears
    # in lst.
    output = 0
    for element in lst:
        if x == element:
            output += 1
    return output

def myInsert( lst, i, x ):
    # Return a new list like lst except that x has been
    # inserted at the ith position.  I.e., the list is now
    # one element longer than before. Print "Invalid index" if
    # i is negative or is greater than the length of lst and 
    # return None.
    if i < 0 or i > len(lst):
        print ("Invalid index")
        return None
    else:
        return lst[:i] + [x] + lst[i:]

def myPop( lst, i ):
    # Return two results: 
    # 1. a new list that is like lst but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is negative or is greater than
    # or equal to len(lst), and return lst unchanged, and None
    if i < 0 or i >= len(lst):
        print("Invalid index")
        return lst, None
    else:
        removedElement = lst[i]
        output = []
        for elementIndex in range(len(lst)):
            if elementIndex == i:
                continue
            else:
                output += lst[elementIndex]
        return output, removedElement

def myFind( lst, x ):
    # Return the index of the first (leftmost) occurrence of 
    # x in lst, if any.  Return -1 if x does not occur in lst.
    if x not in lst:
        return -1
    else:
        output = 0
        for elementIndex in range(len(lst)):
            if lst[elementIndex] == x:
                output = elementIndex
                break
        return output

def myRFind( lst, x ):
    # Return the index of the last (rightmost) occurrence of 
    # x in lst, if any.  Return -1 if ch does not occur in lst.
    if x not in lst:
        return -1
    else:
        output = 0
        for elementIndex in range(len(lst)):
            if lst[elementIndex] == x:
                output = elementIndex
        return output

def myFindAll( lst, x ):
    # Return a list of indices of occurrences of x in lst, if any.
    # Return the empty list if there are none.
    output = []
    if x not in lst:
        return output
    else:
        for elementIndex in range(len(lst)):
            if lst[elementIndex] == x:
                output += [elementIndex]
        return output

def myReverse( lst ):
    # Return a new list like lst but with the elements
    # in the reverse order. 
    return lst[::-1]

def myRemove( lst, x ):
    # Return a new list with the first occurrence of x
    # removed.  If there is none, return lst.
    if x not in lst:
        return lst
    else:
        output = []
        for elementIndex in range(len(lst)):
            if lst[elementIndex] == x:
                output += lst[elementIndex+1:]
                break
            else:
                output += [lst[elementIndex]]
        return output

def myRemoveAll( lst, x ):
    # Return a new list with all occurrences of x
    # removed.  If there are none, return lst.
    if x not in lst:
        return lst
    else:
        output = []
        for element in lst:
            if element == x:
                continue
            else:
                output += [element]
        return output

def myEqual( lst1, lst2 ):
    # Return a Boolean indicating whether the input lists lst1 and lst2 are
    # equal.  Don't use == on the lists; you can use them on
    # individual elements.  Make sure to check that the lengths are equal.
    if len(lst1) != len(lst2):
        output = False
        return output
    else:
        if len(lst1) == 0:
            output = True
        else:
            for elementIndex in range(len(lst1)):
                if lst1[elementIndex] == lst2[elementIndex]:
                    output = True
                else:
                    output = False
                    break
        return output

def allEqual( lst, x ):
    # Return a Boolean indicating whether in list lst all elements, if
    # any, are equal to x.  
    if len(lst) == 0:
        output = True
        return output
    else:
        for element in lst:
           output = element == x
           if output == False:
            break
        return output

# Don't use slicing for this one:
def mySlice( lst, i, j ):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list 
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is 
    # similar but not identical to the way Python slice behaves. 
    if i < 0 or j > len(lst):
        print('Illegal index value')
    else:
        output = []
        while i <= j-1:
            output += [lst[i]]
            i += 1
        return output

def orderedListOfNumbers( lst ):
    # Assume lst is a list of floats.  Return a Boolean indicating all
    # elements (if any) are in ascending order.  It's OK if two successive 
    # elements are equal. 
    if len(lst) == 0:
        output = True
        return output
    else:
        previousValue = lst[0]
        for elementIndex in range(len(lst)):
            nextValue = lst[elementIndex]
            if nextValue >= previousValue:
                previousValue = lst[elementIndex]
                output = True
            else:
                output = False
        return output

 # --------------------------------------------------------------