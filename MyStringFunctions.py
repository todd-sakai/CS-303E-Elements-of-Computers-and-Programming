# Assignment: HW8
# File: MyStringFunctions.py
# Student: Todd Sakai
# UT EID: tfs523
# Course Name: CS303E
# 
# Date: 10.17.25
# Description of Program: Practice with string manipulation functions without using existing str class methods.
def myAppend( s, ch ):
        # Return a new string that is like s but with 
        # character ch added at the end
        return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.
    count = 0
    for i in range(0,len(s)):
        if ch == s[i]:
            count += 1
    return count

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    ans = s1 + s2
    return ans

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    if s == "":
        print("Empty string: no min value")
        return None
    else:
        for ch in s:
            if ch == s[0]:
                min = ch
            elif ord(ch) < ord(min):
                min = ch
        return min

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    if i > len(s):
        print ("Invalid index")
        return None
    else:
        newString = s[0:i] + ch + s[i:len(s)]
        return newString

def myPop( s, i ):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
    newString = ""
    if i >= len(s):
        print ( "Invalid index" )
        return s, None
    else:
        for index in range(0,len(s)):
            if index != i:
                newString += s[index]
        return newString, s[i]

def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(0,len(s)):
        if s[i] == ch:
            ans = i
            break
        else:
            ans = -1
    return ans

def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)-1, -1, -1):
        if s[i] == ch:
            ans = i
            break
        else:
            ans = -1
    return ans

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    if ch not in s:
        return s
    else:
        newString = ""
        for i in range(0,len(s)):
            if s[i] != ch:
                newString += s[i]
            else:
                newString += s[i+1:len(s)]
                break
        return newString

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    if ch not in s:
        return s
    else:
        newString = ""
        for i in range(0,len(s)):
            if s[i] != ch:
                newString += s[i]
        return newString

def myEqual( s1, s2 ):
    # Return a Boolean indicating whether the input strings s1 and s2 are
    # equal.  Don't use == or is on the strings; you can use them on
    # individual characters.
    if len(s1) != len(s2):
        return False
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def myIsdigit( s ):
    # Return a Boolean indicating whether the input string s
    # is nonempty and consists only of decimal digits '0', '1', ..., '9'
    digits = ['1','2','3','4','5','6','7','8','9','0','.']
    if s == "":
        ans = False
    else:
        for i in range(0,len(s)):
            if s[i] not in digits:
                ans = False
                break
            else:
                ans = True
    return ans

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order.  For this one, don't use slicing, 
    # including [::-1].
    ans = ''
    for i in range(len(s)-1, -1, -1):
        ans += s[i]
    return ans

def isPalindrome( s ):
    # Return a Boolean indicating whether the input string s
    # reads the same forward or backward. Case matters: Aba isn't
    # a palindrome.
    backwards = ''
    for i in range(len(s)-1, -1, -1):
        backwards += s[i]
    if len(backwards) != len(s):
        ans = False
    else:
        for i in range(0,len(s)):
            if s[i] != backwards[i]:
                ans = False
                break
            else:
                ans = True
        return ans