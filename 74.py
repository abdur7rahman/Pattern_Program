import string

char = string.ascii_uppercase
n = int(input("Enter the Number: "))
char = " " +char
num = int(n * (n + 1) / 2)

if n <= 26:
    for i in range(1,n+1):
        print(" " * (n - i), end="")        
        for j in range(i,0,-1):
            print(char[num], end=" ")
            num -= 1
        print()

else:
    print("Out of Range!")
    print("The alphabet have Contains only 26 letters")


"""

Enter the Number: 3
  F
 E D
C B A

"""