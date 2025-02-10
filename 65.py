
n = int(input("Enter the No of rows: "))

for i in range(1,n+1):
    print("  " * (n - i),end="")
    for j in range(i,2*i):
        print(j, end=" ")
    for j in range(2*i-2,i-1,-1):
        print(j, end=" ")
    print()

"""

Enter the No of rows: 3
    1
  2 3 2
3 4 5 4 3

"""