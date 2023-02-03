# Dictionary is a collection of key-value pairs


dict = {
    "eat" : "to consume" ,
    "fight"  : "to conflict" ,
    7 : 9 
}

# print(dict['eat'])      # It will print the value of "eat"
# print(dict['fight'])


#       M E T H O D S       #

print(dict.keys())      # Displays the keys 
print(dict.values())    # Displays the values
print(dict.items())     # Displays both in organized form

#  Updating the dictionary 

print(dict)
updict = {
    "moron" : "Mad , Fool , Stupid" 
}

dict.update(updict)
print(dict)

print(dict.get("moron"))    # will print values
print(dict["moron"])

print(dict.get("gando"))        # prints none if there are no keys matching
print(dict["gando"])            # throws an error if the comparable key is not in the dictionary






