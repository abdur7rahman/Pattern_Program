
n = int(input("Enter the No. of Rows: "))
upper = chr(65)
lower = chr(97)

for i in range(1,n+1):
    for j in range(1,i+1):
        
        if (i + j) % 2 == 0:
            print(upper, end=" ")

        else:
            print(lower, end=" ")

        upper = chr(ord(upper) + 1)
        lower = chr(ord(lower) + 1)
    print()

"""

Enter the No. of Rows: 4
A
b C
D e F
g H i J

"""