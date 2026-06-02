# Data types in Python define the type of value a variable can store. 
# They tell the computer whether the data is a number, text, list, etc.
# Types of Data:
# 1.======Immutable Data Types (Cannot be changed after creation)=========
#int,float,str,tuple and boolean

# 2.=======mutable Data Types(Can be changed after creation)=========
#list,dict,and set


#memory interning:it removes the duplication of value and store in single memory location
#example:
# a = 5
# b = 5
# print(id(a)) #140705653359656
# print(id(b))    #140705653359656
# print(a)
# # print(b)

# #=======string immutability check:==========
# name = "saroj"
# print(name.index("s"))
# name[0] = "r"


# lst = ["saroj", "ram", "hari"]
# print(lst[0])
# lst[0] = 1
# print(lst)

#Raw Strings (r''): it skips the escape character and prints as it is as normal string
#syntax:
# r"strings with escape character(\)"

# name = "hel\tlo"
# print(name)
# name = r"hel\vlo"
# print(name)


# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# result = str1 + " " + str2
# print("Combined String:", result)



# x = 10
# print(id(x))   # memory address :140706221556936

# x = 5
# print(id(x)) 



#=============formtting strings concept=================== 
name = "Mr:Skm"
age = 18
weight = 55.5
# %string:
# print("My name is %s, my age is %i and my weight is %.2f kg." %(name,age,weight))


# #.format:
# print("My name is {}, my age is {} and my weight is {} kg.".format(name,age,weight))

# # f-string: (New method)
# print(f"My name is {name}, my age is {age} and my weight is {weight} kg.")

# name = "sushil"
# print(name[0])
# name[0] = "k"
# print(name)


# lst = ["apple", "orange", "123"]
# lst[2] = "banana"
# print(lst)


# a = 5
# b = 5
# print(id(a)) #140711052149800
# print(id(b))    #140711052149800


# name = "hello\tsaroj"
# print(name)  

# name = r"hello\tsaroj"
# print(name)


# firstName = input("Enter your first name:" )
# lastName = input("Enter your last name:" )
# result = firstName +" " + lastName
# print(result)

# name = "mr:Sharma"
# temp = id(name)
# print(id(name))       # Output:1584378059056
# print(temp)


college = "xxavr"
address = "ktm"