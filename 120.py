
n = int(input("Enter the Number of Rows: "))
num = 1
for i in range(1,n+1):
    pattern = [str(num+j) for j in range(i)][::-1]
    print(" " *(n - i) + " ".join(pattern))
    num += i

"""

Enter the Number of Rows: 3
  1
 3 2
6 5 4

"""