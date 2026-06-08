"""
        Dictionary:A dictionary is a built-in data type in Python that stores a collection of data in key-value pairs. 
        Each key is unique and is used to access its corresponding value.
         #It is mutable, ordered, and do not allow duplicate keys.

         #Dictionary is created by curly bracket "{}" and data(key-value pair) is seperated
         by comma. ",".

         syntax:
         dict_var = {
         
                    key1:value1,
                    key2:value2,
                    key3:value2,
         }
         Note:
            key must be unique and immutable data type.

"""
student_name={
    "weight":55.5,
    "height":5.7,
    "class":"bachlor",
    "phone_nu":[9,8030067798]
  
    
    
    
}
student_name["phone_nu"].append(980)
print(student_name["weight"])
print(student_name["height"])
print(student_name["phone_nu"])
"""
        Dictionary:A dictionary is a built-in data type in Python that stores a collection of data in key-value pairs. 
        Each key is unique and is used to access its corresponding value.
         #It is mutable, ordered, and do not allow duplicate keys.

         #Dictionary is created by curly bracket "{}" and data(key-value pair) is seperated
         by comma. ",".

         syntax:
         dict_var = {
         
                    key1:value1,
                    key2:value2,
                    key3:value2,
         }
         Note:
            key must be unique and immutable data type.

"""
#while writing key and value name then use doble or sigle quotes.
student = {
    "name" : "saroj",
    1 : "id1",
    55.55 : "weight", #tree_height
    "age" : 25,
    "gender" : "Male",
    "marks" : [20,40,60,80,[2,4,6]],
    
}

#it access all key- value pair inside the dictonary.
# print(student)   #{'name': 'saroj', 1: 'id1', 55.55: 'weight', 'age': 25, 'gender': 'Male', 'marks': [20, 40, 60, 80]}

# #it access name(Key) values only
# #Syntax:
# # var_name["Key"]

# print(student["name"])  #saroj

# #type function is used to check tyhe data type.
# print(type(student))  # <class 'dict'>


# student["name"] = "Sushil"

# student["marks"].append(50)
# student["marks"][2] = 90
# print(student)


#for deletion
# Syntax:
# del var_name["key"]
# del(var_name["key"])
student = {
    "name" : "saroj",
    1 : "id1",
    55.55 : "weight", #tree_height
    "age" : 25,
    "gender" : "Male",
    "marks" : [20,40,60,80,[2,4,6]],
    
}
del(student["name"])
print(student)
