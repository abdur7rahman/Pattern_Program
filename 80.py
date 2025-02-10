import string

char = string.ascii_uppercase
n = int(input("Enter the No of Rows: "))
num = 0

if n <= 26 and n > 0:
    for i in range(n):
        print(" " * (n - i),end="")
        for i in range(i + 1):
            print(char[num], end=" ")
            num += 1
        num = 0
        print()

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")

"""

Enter the No of Rows: 3
   A
  A B
 A B C

"""