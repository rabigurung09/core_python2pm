""".Write a Python program to convert the string "hello world" into uppercase.

==============Practice Questions for Case Conversion Methods in Strings=================
Q1
Q2.Convert the string "PYTHON PROGRAMMING" into lowercase.

Q3.What will be the output?
    s = "hello python"
    print(s.title())

Q4.Differentiate between title() and capitalize() with example.

Q5.Write a program to capitalize only the first letter of the string "python is fun".

Q6.What will be the output?
    s = "hELLO wORLD"
    print(s.capitalize())

Q7.Write a program to take user input as (name,collegeName,address,favouritePlayer,FavouriteGame) and convert it into:
    •	uppercase 
    •	lowercase 

Q8.What will be the output?
    s = "123abc"
    print(s.upper())

Q9.Correct the following string using proper case (title case):
    s = "welcome to nepal"

Q10.Predict the output:
    s = "python programming"
    print(s.capitalize())
    print(s.title())
"""


"""
#===========Checking Methods (Return True/False)========
Q1. Username Validation

Write a program that takes a username as input and checks:

It contains only alphabets or numbers
It is not empty

Use isalnum() method.



Q2. Password Checker (Basic Rule)

Take a password as input and check:

If it contains only letters → print "Weak Password"
If it contains letters + numbers → print "Medium Password"
If it contains only digits → print "Very Weak Password"

Use isalpha(), isdigit(), isalnum().



Q3. Space Counter Check

Take a sentence from user and check:

Whether the input contains only spaces or not
If yes, print "Only spaces"
Otherwise print "Valid input"

Use isspace().



Q4. Case Checker

Take a string input and check:

If all characters are lowercase → print "Lowercase string"
If all characters are uppercase → print "Uppercase string"
Otherwise → print "Mixed case"

Use islower() and isupper().



Q5. Data Type Analyzer

Take input from user and check:
If input is only digits → print "Number"
If input is only alphabets → print "Text"
If input contains both → print "Alphanumeric"
If input is only spaces → print "Blank input"

Use all: isdigit(), isalpha(), isalnum(), isspace().

Output:
Enter something: 1234
Number: True
Text: False
Alphanumeric: True
Blank input: False

"""
# # Input from user
# text = input("Enter something: ")

# print("Number:", text.isdigit())
# print("Text:", text.isalpha())
# print("Alphanumeric:", text.isalnum())
# print("Blank input:", text.isspace())


# # Password input
# password = input("Enter password: ")

# print("Weak Password (only letters):", password.isalpha())
# print("Very Weak Password (only digits):", password.isdigit())
# print("Medium Password (letters + numbers):", password.isalnum())




# take the five actor name as input and then check its data type and also take  age in interger and then print it in console.
# After that convert name in uppercase,lowercse,capatalize,title).Result print in console.


# Qn. take a username from the user as input then check their case. if they hit uppercase then convert it into lowercse.
# if hit lowercase then convert into uppercase.



# text = input("Enter Your name: ")
# print(text.swapcase())


"""
==========Qn related to (Find , index and count) function  ===========
 Q1. Search Character Position

Write a Python program that:

Takes a string from the user.
Takes one character from the user.
Uses only string functions:
find()
count()
Print:
First position
Total occurrences


Q2. Word Finder Program

Write a Python program that:

Takes a sentence from the user.
Takes a word to search.
Uses only:
find()
index()


Q3. Duplicate Word Counter

Write a Python program that:

Takes a sentence from the user.
Takes a word from the user.
Uses only count() string function.
Print how many times the word appears.


Q4. Email Symbol Checker

Write a Python program that:

Takes an email from the user.
Uses only:
find()
count()
Print:
Position of @
Total number of dots (.)

Q5. String Search Analyzer

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


"""
==========Qn related to (spilt and join) function  ===========
Q1. Full Name Split Program

Write a Python program that:

Takes full name from user
Uses split()
Prints first name and last name separately

firstName: sushil
LastName : singh

Q2. Email Analyzer Program

Write a Python program that:

Takes email from user
Uses split("@")
Prints username and domain name separately


Q3. Website Name Extractor

Write a Python program that:

Takes website URL from user
Uses split(".")
Prints website name only


Q4. Word Join Program

Write a Python program that:

Takes 3 words from user
Stores them in list
Uses join()
Joins all words with space


Q5. CSV Data Split Program

Write a Python program that:

Takes comma-separated values from user
Uses split(",")
Prints each value separately

"""

"""
    =============removing space (strip,lstrip,rstrip) related qn============
Q1. Clean Name Input Program (strip)
Write a Python program that:
Takes a name from user with extra spaces
Removes spaces from both sides using strip()


Q2. Remove Left Side Spaces (lstrip)
Write a program that:
Takes input with left spaces
Removes only left side spaces
    
    
Q3. Remove Right Side Spaces (rstrip)
Write a program that:
Takes input with right spaces
Removes only right side spaces

Q4. Username Cleaner (strip + length)
Write a program that:
Takes username with extra spaces
Removes spaces using strip()
Prints cleaned username and its length


Q5. Password Space Checker (strip logic)
Write a program that:
Takes password input
Removes spaces using strip()
Checks if password was changed after removing spaces
"""



"""
=========suffix related qn =============
Q1. Remove prefix from website

Given string: "www.facebook.com"
Apply removeprefix("www.")

Result: facebook.com

Q2. Remove suffix from domain

Given string: "google.com"
Apply removesuffix(".com")

Result: google

Q3. Remove title prefix

Given string: "Mr. Saroj"
Apply removeprefix("Mr. ")

Result: Saroj

Q4. Remove file extension

Given string: "notes.txt"
Apply removesuffix(".txt")

Result: notes

Q5. Remove both prefix and suffix

Given string: "www.python.org"
Apply removeprefix("www.") and removesuffix(".org")

Result: python
    
"""
    






    
# name = input("enter your name:")
# result = name.split(" ")
# # print(result)
# print("first Name:", result[0])
# print("first Name:", result[1])


# text = "Mr.Saroj"
# print(text.removeprefix("."))


# text = "I like Java"
# result = text.replace("Java", "Python")
# print(result)

# fullname = input("Enter your fullName: ")
# text = fullname.split(" ")
# print(text)
# print("first Name: ",text[0])
# print("lastName: ", text[1])


# txt = "banana"
# x = txt.rjust(20)

# print(x, "is my favorite fruit.")


# txt = "banana"
# x = txt.ljust(50)
# print(x, "is my favorite fruit.")

# txt = "banana"
# x = txt.center(20)
# print(x, "is my favorite fruit.")