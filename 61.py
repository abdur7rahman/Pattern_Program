n = int(input("Enter the Length od Square: "))

for i in range(1,n+1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("*" + "  " * (n -2) + " *")

"""

Enter the Length od Square: 5
* * * * *
*       *
*       *
*       *
* * * * *

"""