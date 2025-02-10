
import string

char = " " + string.ascii_uppercase
n = int(input("Enter the Number: "))

if n <= 26:
    for i in range(1,n + 1):
        print((char[i] + " ") * n)

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")

"""

Enter the Number: 3
A A A
B B B
C C C

"""