
n = int(input("Enter the No of Rows: "))

for i in range(1,n+1):
    print("  " * (n - i), end=" ")
    for j in range(i,0,-1):
        print(j, end=" ")
    for j in range(2,i+1):
        print(j, end=" ")
    print()

"""

Enter the No of Rows: 4
       1 
     2 1 2 
   3 2 1 2 3 
 4 3 2 1 2 3 4 

"""