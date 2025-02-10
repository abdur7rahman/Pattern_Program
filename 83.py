n = int(input("Enter the No of Rows: "))

for i in range(1,n+1):
    for j in range(i,i+1):
        print("* "*i + "  "*(n - i), end="")

    for j in range(i,i+1):
        if i == n:
            print("* "*(n-1))

        else:
            print("  "*(n - i - 1) + "* "*i)

for i in range(n-1,0,-1):
    for j in range(i,i+1):
        print("* "*i + "  "*(n - i), end="")

    for j in range(i,i+1):
        print("  "*(n - i - 1) + "* "*i)

"""

Enter the No of Rows: 3
*       *
* *   * *
* * * * *
* *   * *
*       *

"""