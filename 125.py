
n = int(input("Enter the Number of Rows: "))
for i in range(1,n+1):
    for _ in range(1,i+1):
        print(2*(i)-1,end=" ")
    print()

"""

Enter the Number of Rows: 4
1
3 3
5 5 5
7 7 7 7

"""