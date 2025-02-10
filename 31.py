import string

char = string.ascii_uppercase
n = int(input("Enter the Number: "))
char = " " +char

if n <= 26:
    for i in range(1,n + 1):
        for j in range(1,i+1):
            print(char[j], end=" ")
        print()

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")

"""

Enter the Number: 3
A
A B
A B C

"""