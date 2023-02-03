# ***       to print this pattern for n = 3
# **
# *


n = int(input("Enter n " ))

def pattern(size) :
 for i in range(size):
    print("*" *(size-i))
    
pattern(n)

