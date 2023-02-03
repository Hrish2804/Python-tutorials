a = "hrishi"

# To access any elemnt of the string we can use "a[n]" 

# print(a[3])
# print(a[1])

 
# # Now we have to slice string which is done using a[_:_] --> 1st '_' represents inital location and 2nd one states the final location ,, ' : " means 'to'
# # i.e from 1--> 3 

# print(a[1:4])
# print(a[0:2])

# print("Giving only initial value a[0:] :  ", a[0:])        # it will take the last value of the string
# print("Giving only the last value a[:4] : " , a[:4])       # It is initially 0 by default

# #  This can be counted negatively too --> value = length-1

# print("a[-3:-1] : " , a[-3:-1])                # It is same as a[4:5]
# print( "a[-1:-4] : " , a[-4:-1])               # i.e same as a[3:5]

a = "HrishIsDesparate"

print(" Using a[0:0:2] : ", a[0::3])            # a[initial value : last value : value to skip] (Here skip value = 3 so after 3 letters the character will be skiped) --> if any of begin or end value is not given, it will be '0' and 'length' by default

print("a[0:5:2] : " , a[0:5:2])