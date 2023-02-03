# A set is a collection of non-repetitive elements 

#  a = {1,2,3,4,1}
# print(a)

# # If we try to declare an empty set using b={} ~~
# b = {}
# print(type(b))      # Empty dictionary will be created 

# So in order to create an empty set we will use 'c=set()'
# c = set()
# print(type(c))      # This will now be called as empty set


#       M E T H O D S        #

# # To add values in set we use ' .add() ' method
# c.add(4)
# c.add(5)
# print(c)

# Even by adding values externally repetition wont occur


# ## So now we will try to create a list inside set to check whether it will support repetition
# d = {[4,3,4,5]} 
# print(d)        # Throws an error


# Finding the length of set
a = {1 , 3 , 5 , 4}
# print(len(a))

# # Removing an element
# a.remove(1)
# print(a)

# a.remove(6)
# print(a)


# # Removing any random value
# a.pop()
# print(a)

# # To clear whole set , we use 'a.clear()'
# a.clear()
# print(a)


# # Union of sets --> By using 'a.union({4,5,6})
# a = a.union({4,5,6})
# print(a)

# Intersection !
a = a.intersection({4 , 2 , 8 })

print(a)





 






