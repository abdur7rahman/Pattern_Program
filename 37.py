
import string

char = string.ascii_uppercase
n = int(input("Enter the Number: "))
char = " " +char
if n <= 26:
    for i in range(n,0,-1):
        print(" " * (n - i) + (char[i] + " ") * i)

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")

"""

Enter the Number: 3
C C C
 B B
  A

"""