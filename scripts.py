
# Exercicios com if, elif, else. 
"""
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird"""

n = int(input(': '))

if n % 2 == 1:
    print('Weird')

elif n % 2 == 0 and n in range(2, 6):
    print('Not Weird')

elif n % 2 == 0 and n in range(6, 21):
    print('Weird')

else:
    print('Not Weird')

# Codigo com pequena correção. Necessario possivel refatoração


# Exercicios com loops
"""
Task
The provided code stub reads and integer, , from STDIN. For all 
non-negative integers i < n, print i²."""

n = int(input(': '))

for i in range(n):
    print(i**2)
# """
# i **= 2
# print(i) # Parte refatorada do codigo
# Codigo final

# Exercicio com int e strings
"""
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between
"""

n = int(input(': '))

for i in range (1, n+1):
    print (i, end="") # Usa a função 'end=""' para organizar o valor em linha
# Codigo completo


    
""""
An extra day is added to the calendar almost every four years as February 29, 
and the day is called a leap day. It corrects the calendar for the fact that our 
planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
 while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.                             
"""
# Exercio com função e condicionais 
# Codigo passa nos teste, mas precisa de refatoração

def is_leap(year):
    leap = False
    if year % 400 == 0 or year % 4 == 0 and year < 2000:
        leap = leap
        return True
    elif year % 100 == 0:
        leap = leap
        return False
    return leap
# Codigo completo sem refatoração 


# Compressão de listas
# Test Case
x = int(input(': '))
y = int(input(': '))
z = int(input(': '))
n = int(input(': '))

"""
Dado valores para x, y e z usa compressão de lista
para imprimir grade 3d em que os somatorios de x, y, z
sejam diferentes de n
"""

print ([[i,j,k] for i in range(0,x+1) for j in 
range(0,y+1) for k in range(0,z+1) if i + j + k != n ])








