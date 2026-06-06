
"""==========Qn related to (spilt and join) function  ===========
Q1. Full Name Split Program

Write a Python program that:

Takes full name from user
Uses split()
Prints first name and last name separately

firstName: sushil
LastName : singh"""
user=input("enter your name : ")
text=user.split()
print(text[0])
print(text[-1])

"""Q2. Email Analyzer Program

Write a Python program that:

Takes email from user
Uses split("@")
Prints username and domain name separately


Q3. Website Name Extractor

Write a Python program that:

Takes website URL from user
Uses split(".")
Prints website name only
"""
user=input("enter your email : ")
text=user.split(".")
print(text[0])
print(text[1])
user=input("enter website url : ")
text=user.split(".")
print(text[1])
"""4. Word Join Program

Write a Python program that:

Takes 3 words from user
Stores them in list
Uses join()
Joins all words with space"""
user=input("enter 3 word : ")
text=user.split()
text_1="".join(text)
print(text,"\n",text_1,sep="")

"""Q5. CSV Data Split Program

Write a Python program that:

Takes comma-separated values from user
Uses split(",")
Prints each value separately"""
user=input("enter value with comma : ")
text=user.split(",")
print(text[0])
print(text[1])







