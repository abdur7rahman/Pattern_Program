

n = int(input("Enter the No of Rows: "))
temp = 0
for i in range(1,n+1):
    print("  "*(temp), end="")
    temp +=1
    for j in range(i,n+1):
        print(j, end=" ")
    print()

"""

Enter the No of Rows: 3
1 2 3
  2 3
    3

"""