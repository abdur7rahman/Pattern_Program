
n = int(input("Enter the Number of Rows: "))
for i in range(1,n+1):
    for _ in range(1,i+1):
        print(2*(i),end=" ")
    print()

"""

Enter the Number of Rows: 4
2
4 4
6 6 6
8 8 8 8

"""