word = input("Enter the Word: ")

for i in range(1,len(word)+1):
    print(" "*(len(word) - i) + word[0:i])

"""

Enter the Word: two
  t
 tw
two

"""