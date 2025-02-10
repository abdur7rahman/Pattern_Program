
n = int(input("Enter the No of Rows: "))

for i in range(1,n+1):
    if i == n:
        for j in range(1,2*n):
            print(j%2,end=" ")
        print()

    else:
        for j in range(1,i+1):
            print(j%2,end=" ")

        print("  "* ((2*(n-i))-1), end="")
        for j in range(i,0,-1):
            print(j%2, end=" ")
        print()

for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j%2,end=" ")

    print("  "* ((2*(n-i))-1), end="")
    for j in range(i,0,-1):
        print(j%2, end=" ")
    print()

"""

Enter the No of Rows: 3
1       1
1 0   0 1
1 0 1 0 1
1 0   0 1
1       1

"""