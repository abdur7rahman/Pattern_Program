
n = int(input("Enter the No of Rows: "))
num = 0
lower, upper = 0, 0
for i in range(1,n+1):
    for j in range(i):
        if num % 2 == 0:
            print(chr(65+upper), end=" ")
            num +=1
            upper += 2
        else:
            print(chr(98+lower), end=" ")
            num +=1
            lower +=2
    print()

"""

Enter the No of Rows: 4
A
b C
d E f
G h I j

"""