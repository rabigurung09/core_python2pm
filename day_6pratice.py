personal_name="rabi gurung"
college_name="universal college"
print(personal_name,"\n",college_name,sep="")
# output:
# rabi gurung
# universal college
"""Qn related to (Find , index and count) function  ======
 Q1. Search Character Position

Write a Python program that:

Takes a string from the user.
Takes one character from the user.
Uses only string functions:
find()
count()
Print:
First position
Total occurrences"""
user=input("enter a string :")
user_1=user[0:1]
print(user.count(user_1))
print(user_1)
# output:
# 3
# i
rab_1=input("Enter a string")
user_1=input("Enter a char to find its index")
text=rab_1.find(user_1)
text_2=rab_1.count(user_1)
print(text,"\n",text_2,sep="")
"""Q2. Word Finder Program

Write a Python program that:

Takes a sentence from the user.
Takes a word to search.
Uses only:
find()
index()
"""
user=input("enter a sentence : ")
user_1=input("enter a word to search : ")
text=user.find(user_1)
text_2=user.index(user_1)
print(text,"\n",text_2,sep="")
"""Q3. Duplicate Word Counter

Write a Python program that:

Takes a sentence from the user.
Takes a word from the user.
Uses only count() string function.
Print how many times the word appears."""
user=input("enter a sentence : ")
user_1=input("enter a word to search : ")
print(user.count(user_1))
"""Q4. Email Symbol Checker

Write a Python program that:

Takes an email from the user.
Uses only:
find()
count()
Print:
Position of @
Total number of dots (.)
"""
user=input("enter a gmail : ")
text="@"
text_2="."
print(user.find(text))
print(user.count(text_2))
"""Q5. String Search Analyzer

Write a Python program that:

Takes a string from the user.
Takes a search word.
Uses only string functions:
find()
index()
count()
Print:
First position
Index position
Total occurrences
"""
user=input("enter a string")
user_1=input("enter a word to search")
print(user.find(user_1))
print(user.count(user_1))
print(user.index(user_1))
