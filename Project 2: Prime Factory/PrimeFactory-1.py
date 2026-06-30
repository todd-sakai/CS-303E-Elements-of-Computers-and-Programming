# Assignment: Project 2
# File: PrimeFactory.py
# Student: Todd Sakai
# UT EID: tfs523
# Course: C S 303E
# 
# Date: 11.16.25
# Description of Program: 

# Imports
import math

# Global constants
EXIT_PHRASES = ["0", "exit", "quit", "leave"]
HELP_PHRASES = ["6", "help", "info"]

# Function definitions
def IS_PRIME(N):
    isPrime = True
    if ( N % 2 ==0 ):
        isPrime = (N == 2)
    else:
        divisor = 3
        while (divisor <= math.sqrt(N)):
            if (N % divisor == 0):
                isPrime = False
                break
            else:
                divisor += 2
    return isPrime

def LIST_N_PRIMES(N):
    list_of_n_primes = []
    num = 0
    for i in range (N):
        next_prime = FIRST_PRIME_AFTER(num)
        list_of_n_primes.append(next_prime)
        num = next_prime
    return list_of_n_primes

def SHOW_NTH_PRIME(N):
    return LIST_N_PRIMES(N)[-1]

def FIRST_PRIME_AFTER(N):
    if (N < 2):
        return 2
    if (N % 2 == 0):
        N -= 1
    guess = N + 2
    while (not IS_PRIME(guess)):
        guess += 2
    return guess

def FACTOR(N):
    list_of_factors = []
    d = 2
    while IS_PRIME(N) == False and N > 1:
        while N % d == 0:
            list_of_factors.append(d)
            N //= d
        d = FIRST_PRIME_AFTER(d)
    if IS_PRIME(N) == True or N == 1:
        if N != 1:
            list_of_factors.append(N)
    return list_of_factors

def HELP():
    print("The following commands are available:")
    print("  0: Exit.")
    print("  1: Is N a prime?")
    print("  2: List the first N prime numbers.")
    print("  3: Display the Nth prime number (1-based).")
    print("  4: Find first prime after N.")
    print("  5: Factor N.")
    print("  6: Display this help message.")

def VALIDATE_INPUT(prompt, N):
    if prompt == 1 or prompt == 3:
        if N <= 0:
            return False
    elif prompt == 2:
        if N < 0:
            return False
    elif prompt == 5:
        if N < 2:
            return False
    else:
        return True

# Main function definition
def main():
    print("Welcome to the Prime Factory!")
    HELP()

    while True:
        print()
        command = input("Please enter a command: ").lower().strip()

        if command in EXIT_PHRASES:
            print ("Thanks for visiting our factory! Goodbye.")
            break

        elif command == "1":
            print("You've asked if N is a prime.")
            N = input("What is N? ")
            if VALIDATE_INPUT(1,int(N)) == False:
                print("Illegal value. Try again!")
            else:
                if IS_PRIME(int(N)) == True:
                    print(N, "is prime")
                else:
                    print(N, "is not prime")

        elif command == "2":
            print("You've asked to display the first N prime numbers.")
            N = input("What is N? ")
            if VALIDATE_INPUT(2,int(N)) == False:
                print("Illegal value. Try again!")
            else:
                print ("The first " + N + " primes are:", LIST_N_PRIMES(int(N)))
        
        elif command == "3":
            print("You've asked for the Nth prime number.")
            N = input("What is N? ")
            if VALIDATE_INPUT(3,int(N)) == False:
                print("Illegal value. Try again!")
            else:
                print ("The " + N + "th prime is:", SHOW_NTH_PRIME(int(N)))

        elif command == "4":
            print("You've asked for the first prime number after N.")
            N = input("What is N? ")
            if VALIDATE_INPUT(4,int(N)) == False:
                print("Illegal value. Try again!")
            else:
                print ("The first prime after " + N + " is:", FIRST_PRIME_AFTER(int(N)))

        elif command == "5":
            print("You've asked for the prime factorization of N.")
            N = input("What is N? ")
            if VALIDATE_INPUT(5,int(N)) == False:
                print("Illegal value. Try again!")
            else:
                print ("The prime factorization of " + N + " is:", FACTOR(int(N)))

        elif command in HELP_PHRASES:
            HELP()
        
        else:
            print("Command " + command + " not recognized. Try again!")
            print()
            HELP()

# Call to main function
main()