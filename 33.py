
n = int(input("Enter the NUmber: "))

for i in range(1,n+1):
    print("  " * (n - i) + "* " * (2 * i -1))

"""

Enter the NUmber: 3
    *
  * * *
* * * * *

"""