
n = int(input("Enter the No of Rows: "))
temp = 0
for i in range(1,n+1):
        if i == 1:
            print(" "* (n -i) + "*")
        elif i ==2:
            print(" " * (n - i) + "* " * i)
        else:
            print((n - i) * " " + "*" + (i + temp)* " " + "*")
            temp +=1
temp = n-4
for i in range(n-1,0,-1):
        if i == 1:
            print(" "* (n -i) + "*")
        elif i ==2:
            print(" " * (n - i) + "* " * i)

        else:
            print((n - i) * " " + "*" + (i + temp)* " " + "*")
            temp -=1

"""

Enter the No of Rows: 3
  *
 * *
*   *
 * *
  *

"""