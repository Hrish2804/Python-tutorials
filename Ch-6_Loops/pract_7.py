# for n = 3 , Printing 

#     *
#    ***
#   ***** 

n = int(input("Enter n "))

for i in range(n):      
    print(" " *(n-i-1) , end="") 
    print("*"*(2*i+1) , end ="")
    print(" " *(n-i-1) )
  
