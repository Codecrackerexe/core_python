def get_input():
    print()
    return int(input("Enter the number of rows: "))
#=================================================>
# Increasing star half pyramid
n = get_input()
for i in range(1, n+1):
    print('*' * i)
#=================================================>
# Decreasing star half pyramid
n = get_input()
for i in range(n):
    print(' ' * (n-i-1) + '*' * (i+1))
#=================================================>
# Star pyramid Pattern
n = get_input()
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
#=================================================>
# Increasing Number half pyramid
n = get_input()
for i in range(n):
    for j in range(1, i+2):
        print(j, end=' ')
    print()
#=================================================>
# Decreasing Number half pyramid
n = get_input()
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
#=================================================>
# Number pyramid
n = get_input()
for i in range(n):
    print(' ' * (n-i-1), end=' ')
    for j in range(1, 2*i+2):
        print(j, end='')
    print()
#=================================================>
# Increasing Alphabet half pyramid
n = get_input()
for i in range(65, 65+n):
    for j in range(65, i+1):
        print(chr(j), end=' ')
    print()
#=================================================>
# Decreasing Alphabet half pyramid
n = get_input()
for i in range(n):
    print(' ' * (n-i-1), end='')
    for j in range(65, 65+i+1):
        print(chr(j), end=' ')
    print()
#=================================================>
# Alphabet repeating half pyramid
n = get_input()
for i in range(65, 65+n):
    print(chr(i) * (i-64))
print()
