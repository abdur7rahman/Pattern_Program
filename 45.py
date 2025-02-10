
n = int(input("Enter the No. of Rows: "))
num = 1
for i in range(1,n+1):
    print(" " * (n - i), end="")
    for j in range(1,i+1):
        print(num, end=" ")
        num += 1
    print()

"""

Enter the No. of Rows: 3
  1
 2 3
4 5 6

"""