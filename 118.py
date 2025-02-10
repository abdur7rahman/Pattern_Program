
n = int(input("Enter the No of Rows: "))
nums = [i for i in range(1,n+1)]
for i in range(len(nums)):
    print(*nums)
    nums = nums[1:] + nums[:1]

"""

Enter the No of Rows: 4
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3

"""