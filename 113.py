n = int(input("Enter the rows: "))

for i in range(n,0,-1):
    print("  " * (n - i), end=" ")
    for j in range(1,i+1):
        print(j % 2, end=" ")
    print()

"""

Enter the rows: 3
 1 0 1
   1 0
     1

"""