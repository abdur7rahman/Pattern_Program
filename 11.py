
n = int(input("Enter the Number: "))

for i in range(n,0,-1):
    print(" " * (n - i) + "* " * i)

"""

Enter the Number: 3
* * *
 * *
  *

"""