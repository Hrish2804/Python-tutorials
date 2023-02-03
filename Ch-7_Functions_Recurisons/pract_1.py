# To print sum of n natural numbers using recursion

def sum(n) :

    if(n==0) : 
        return 0
    
    sumn = n + sum(n-1)
    return sumn

n = int(input("Enter n "))
result = sum(n)
print("Sum of n = " ,result)