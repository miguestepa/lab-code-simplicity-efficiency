"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

#First of all: I like to find some comments when I see code.

import random

def RandomStringGenerator(c, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    s = ''
    #here is better just to use a 'for loop'. 'While loops' can generate more problems.
    for i in range(c):
         #For me it is more correct to call a library at the beginning of the code, so you only call it once. I move 'random' to the first lines.
        s += random.choice(a)
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:

            #For me it is more correct to call a library at the beginning of the code, so you only call it once. I move 'random' to the first lines.
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

# Since these are going to be the most important variables of this program, I prefer to see them at the beginning of the code, right after imported packages.
a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
