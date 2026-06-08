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