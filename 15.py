
n = int(input("Enter the Number: "))

for i in range(1,n+1):
    print(" " * (n - i) + (str(i) + " ") * i)

for i in range(n-1,0,-1):
    print(" " * (n - i) + (str(i) + " ") * i)

"""

Enter the Number: 3
  1
 2 2
3 3 3
 2 2
  1

"""