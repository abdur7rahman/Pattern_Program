
n = int(input("Enter the Number: "))

for i in range(n,0,-1):
    print(" " * (n - i) + (str(i) + " ") * i)

"""

Enter the Number: 3
3 3 3
 2 2
  1

"""