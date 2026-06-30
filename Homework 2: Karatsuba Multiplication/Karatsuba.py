# Assignment: HW2
# File: Karatsuba.py
# Student: Todd Sakai 
# UT EID: tfs523
# Course: C S 303E
# 
# Date: 9.9.25
# Description of Program: Implements a special case of Karatsuba multiplication for two 4-digit integers input by the user

def main():
    n1 = int( input("Enter a 4-digit integer: ") )
    n2 = int( input("Enter a 4-digit integer: ") )
    
    a=int(n1/100)
    b=int(n1%100)
    
    c=int(n2/100)
    d=int(n2%100)

    e=int(a*c)
    f=int(b*d)

    g=int((a+b)*(c+d))

    h=int(g-(e+f))

    i=int((e*(10**4)))

    j=int((h*(10**2)))

    k=int((i+j+f))

    ans=int((n1*n2))

    print("Computed result:",(k))
    print("Expected result:",(ans))
