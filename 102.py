
n = int(input("Enter the Number: "))

for i in range(1,n+1):
    print(" " * (n - i) + (str(i%2) + " ") * i)

"""

Enter the Number: 3
  1
 0 0
1 1 1

"""