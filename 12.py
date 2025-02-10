
n = int(input("Enter the Number: "))

for i in range(1,n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1,0,-1):
    print(" " * (n - i) + "* " * i)

"""

Enter the Number: 3
  *
 * *
* * *
 * *
  *

"""