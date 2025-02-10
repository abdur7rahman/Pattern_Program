n = int(input("enter the No of Rows: "))
num = int(n * (n+1)/2)

for i in range(1,n+1):
    print(" "* (n - i),end="")
    for j in range(i,0,-1):
        print(num, end=" ")
        num -=1
    print()

"""

enter the No of Rows: 3
  6
 5 4
3 2 1

"""