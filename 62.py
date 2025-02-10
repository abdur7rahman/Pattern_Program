n = int(input("Enter the Length of rectangle: "))

for i in range(1,n-1):
    if i == 1 or i == n-2:
        print("* " * (n+1))
    else:
        print("*" + "  " * (n -2) + "   *")

"""

Enter the Length of rectangle: 5
* * * * * *
*         *
* * * * * *

"""