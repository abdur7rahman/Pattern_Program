
import string

char = string.ascii_uppercase
n = int(input("Enter the Number: "))
char = " " +char
num = 1

if n <= 26:
    for i in range(1,n + 1):
        for j in range(1,i+1):
            print(char[num], end=" ")
            num += 1
        print()

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")

"""

Enter the Number: 3
A
B C
D E F

"""