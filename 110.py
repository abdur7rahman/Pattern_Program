
n = int(input("Enter the No of Rows: "))

temp = n-4
for i in range(n,0,-1):
        if i == 1 :
            print(" "* (n -i) + "*")
        elif i ==2:
            print(" " * (n - i) + "* " * i)
        elif i == n:
            print("* " * n)
        else:
            print((n - i) * " " + "*" + (i + temp)* " " + "*")
            temp -=1

temp = 0
for i in range(2,n+1):
        if i == 2:
            print(" " * (n - i) + "* " * i)
        elif i == n:
            print("* " * n)
        else:
            print((n - i) * " " + "*" + (i + temp)* " " + "*")
            temp +=1

"""

Enter the No of Rows: 4
* * * *
 *   *
  * *
   *
  * *
 *   *
* * * *

"""