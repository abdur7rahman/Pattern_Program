import string

char = string.ascii_uppercase
n = int(input("Enter the number of rows (up to 26): "))

if 1 <= n <= 26:
    for i in range(1,n+1):
        for j in range(n - i, n):
            print(char[j], end=" ")
        print()
else:
    print("Out of Range! The alphabet contains only 26 letters.")
    print("The alphabet have Contains only 26 letters")

"""

Enter the number of rows (up to 26): 3
C
B C
A B C

"""