import string

char = string.ascii_uppercase
n = int(input("Enter the Number: "))

if n <= 26 and n > 0:
    for i in range(n,0,-1):
        print("  " * (n - i),end="")
        for j in range(i):
            print(char[j], end=" ")
        print()

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")

"""

Enter the Number: 3
A B C
  A B
    A

"""