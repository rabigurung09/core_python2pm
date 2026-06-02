#============Strings Property=====================
#1. concatination property(+): it joins the two strings.
# syntax:
# var1 + var2
# in above syntax there is two varible and it is concatenated(join) with (+) symbol.



#example:
# var1 = "car"
# var2 = "toyta"
# result = var1 + var2
# print(result)
# # print("car"," ","toyta")          #cartoyta
# print("car","toyta", sep=" ")       #car toyta

# num = "1"
# num1 = "2"
# result = num + num1
# print(result)       #12


#2.====id:it  gives the memory address where the data(value) is located.

# name = "saroj"
# rollNo = 5
# weight = 55.5
# print(id(name))
# print(id(rollNo))
# print(id(weight))

#3. indexing:it acess the string character by using index value. 
#example:
# name = "saroj"
# name[0]

# num = "12345"
# print(num[3]) # 4

# num = "12345"
# print(num[2]) #3
# print(num[8])  # error


#4. len():
# name = "saroj"
# print(len(name)) #5

#5. input():

#6.=======================slicing():========================================
'''
Slicing:
        process of accessing the parts(portions) of sequence data type(string,list,tuple,etc.)
        syntax:
        varName[start_index:end_index:step]   

        Note: 
        # end_index value is not included.
        # By default, step = 1
'''
#====== +ve slicing ==========
# name = "saroj"
# address = "Bhaktapur"
# # text = name[0:3]  
# text = name[0::3]
# print(text)

# print(address[3:6])  #kta

# book = "encyclopedia"  # output:"ncy","ope","nclop"

#====== -ve slicing ==========
# name = "saroj"
# address = "Bhaktapur"
# print(address[:4])


# print(name[-3:-1])  #Output:
# print(name[-3::])   #Output:

# book = "encyclopedia"  # output:"ncy","ope","nclo","ncylo"


# 5.Write a program to take a string from the user and print:
#     Characters from index 2 to 6
#     Characters from -5 to -1
user = input("Enter any String: ")


# 1.Write a program to take a string from the user and print the first character, second character, and last character using indexing.
user = input("Enter any string: ")
print(user[0])
print(user[1])
print(user[-1])

