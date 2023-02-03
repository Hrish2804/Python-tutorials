# To find whether a number is prime or not
n = int(input("Enter number : "))
prime = True

for i in range(2,n) :           # If it has only one multiple which is itself cuz the other first is already not considered. It leaves another multiple.
    if(n%i==0) :
        prime = False
        break

if prime :
    print("Prime")

else :
    print("Not prime")
       








