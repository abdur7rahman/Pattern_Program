
n = int(input("Enter the No. of rows: "))

for i in range(1,n + 1):
    print("  " * (n - i), end=" ")
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

"""

Enter the No. of rows: 3
     1
   2 1
 3 2 1

"""