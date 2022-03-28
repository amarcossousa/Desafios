"""
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird"""

# n = int(input('Entre com um valor inteiro: '))

# if n % 2 == 0 and n <= 2:
#     print('Weird')
# else: 
#     print('Not Weird')

# if n % 2 == 1 and n > 2 <= 5:
#     print('Not Weird')
# else:
#     print('Weird')

# elif n % 2 == 0 and n > 2 <= 5:
#     print('Not Weird')

# elif n % 2 == 0 and n > 6 <= 20:
#     print('Weird')

# if n % 2 == 1 and n > 24:
#     print('Not Weird')

# else:
#     print('Not Weird')

n = int(input())
cont = 0
while cont < n:
    n = n + 1
    print(n)

# n = int(input("Numero"))
# cont = 0
# while n >=cont:
#     print(n)
