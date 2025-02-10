
n = int(input("Enter the No. of rows: "))

for i in range(n,0,-1):
    print("  " * (n - i), end=" ")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

"""

Enter the No. of rows: 3
 3 2 1
   2 1
     1

"""