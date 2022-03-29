# Exercicios com if, elif, else. 
"""
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird"""

n = int(input(': '))

if n % 2 == 0 and n < 2:
    print('Weird')

elif n % 2 == 1 and n in range(2,  6) or n > 20:
    print('Not Weird')

else:
    print('Weird')
# Codigo não funciona em alguns testes no HackerRanck


# Exercicios com loops
"""
Task
The provided code stub reads and integer, , from STDIN. For all 
non-negative integers i < n, print i².
"""

n = int(input(': '))

for i in range(n):
    print(i**2)
    # i **= 2
    # print(i)
# Codigo final