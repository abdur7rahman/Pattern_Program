n = int(input("enter the No of Rows: "))
num = 1

for i in range(n,0,-1):
    print("  "* (n - i),end="")
    for j in range(i,0,-1):
        print(num, end=" ")
        num +=1
    print()

"""

enter the No of Rows: 3
1 2 3
  4 5
    6

"""