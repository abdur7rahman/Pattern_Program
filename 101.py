
n = int(input("Enter the No of Rows: "))

for i in range(1,n+1):
    print("  "*(n-i), end="")
    for j in range(i,0,-1):
        print(j%2, end=" ")
    print()

for i in range(n-1,0,-1):   
    print("  "*(n-i), end="")
    for j in range(i,0,-1):
        print(j%2, end=" ")
    print()

"""

Enter the No of Rows: 3
    1
  0 1
1 0 1
  0 1
    1

"""