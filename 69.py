
import string

n = int(input("Enter the No. of rows: "))
char = " " + string.ascii_uppercase

if n >= 26:
    for i in range(n,0,-1):
        print(" " * (n - i), end="")
        for j in range(i,0,-1):
            print(char[j], end=" ")
        print()

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")
    
"""

Enter the No. of rows: 3
C B A
 B A
  A

"""