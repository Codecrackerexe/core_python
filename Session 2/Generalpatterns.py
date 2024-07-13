# Increasing star half pyramid
n = int(input("Enter the number of rows:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
#====================================>
# Decreasing star half pyramid
print()
n = int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(1, n - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("*", end="")
    print()
#====================================>
# Star pyramid Pattern
print()
n = int(input("Enter the number of rows:"))
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
#====================================>
# Increasing Number half pyramid
print()
n= int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
#====================================>
# Decreasing Number half pyramid
print()
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
#====================================>
#  Number pyramid
print()
n= int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print(k+1, end=" ")
    print() 
#====================================>
# Increasing Alphabet half pyramid
print()
n= int(input("Enter the number of rows:"))
for i in range (65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()
#====================================>
# Decreasing Alphabet half pyramid
print()
k = 64
print("The pattern of decreasing alphabet half pyramid is as follows:")
for i in range(65, 70):
    for j in range(69, 64, -1):
        if(j <= i):
            k += 1;
            a = chr(k)
            print(a, end=" ")
        else:
            print(" ", end=" ")
    print()
#====================================>
#  Alphabet repeating half pyramid
print()
print("The repeating alphabet half pyramid is as follows:")
for i in range(65, 70):
    for j in range(64, i):
        a = chr(i)
        print(a, end="")
    print()

  

