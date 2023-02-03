# To replace a formal letter :- 

# Dear <name> ,
# Good morning ,
#     You are selected for the interview , so be ready with your stuff (i know its informal , i am just kidding !!).
# <date> 

#   Write a program in such a manner that user inputs name and date and the value in  the letter gets changed as per the input

letter = '''Dear <name> ,
Good morning ,
    You are selected for the interview , so be ready with your stuff (i know its informal , i am just kidding !).
<date> 
'''
# Without writing program
print(letter)

name = input("Enter name : \n")
date = input("Enter date : \n")
letter = letter.replace("<name>" , name)
letter = letter.replace("<date>" , date)

print(letter)