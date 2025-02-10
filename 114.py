
n = int(input("Enter the No. of rows: "))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j%2, end=" ")
    print()

"""

Enter the No. of rows: 3
1 0 1
0 1
1

"""