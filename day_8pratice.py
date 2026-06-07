'''=============removing space (strip,lstrip,rstrip) related qn============
Q1. Clean Name Input Program (strip)
Write a Python program that:
Takes a name from user with extra spaces
Removes spaces from both sides using strip()
'''
user=input("enter your name : ")
text=user.strip( )
text_1=user.lstrip( )
text_2=user.rstrip( )
print(text)
print(text_1)
print(text_2)

"""Q2. Remove Left Side Spaces (lstrip)
Write a program that:
Takes input with left spaces
Removes only left side spaces
"""
user=input("enter your name : ")
text=user.lstrip()
print(text)
"""Q3. Remove Right Side Spaces (rstrip)
Write a program that:
Takes input with right spaces
Removes only right side spaces"""
user=input("enter your name : ")
text=user.rstrip()
print(text)
"""Q4. Username Cleaner (strip + length)
Write a program that:
Takes username with extra spaces
Removes spaces using strip()
Prints cleaned username and its length
"""
user=input("enter your name : ")
text=user.strip()
print(len(text))
"""Q5. Password Space Checker (strip logic)
Write a program that:
Takes password input
Removes spaces using strip()
Checks if password was changed after removing spaces"""
user=input("enter your password : ")
text=user.strip()
print(text)
"""=========suffix related qn =============
Q1. Remove prefix from website

Given string: "www.facebook.com"
Apply removeprefix("www.")

Result: facebook.com"""
user="www.facebook.com"
text=user.removeprefix("www.")
print(text)
"""Q2. Remove suffix from domain

Given string: "google.com"
Apply removesuffix(".com")

Result: google
"""
user="google.com"
text=user.removesuffix(".com")
print(text)
"""Q3. Remove title prefix

Given string: "Mr. Saroj"
Apply removeprefix("Mr. ")

Result: Saroj"""
user="Mr. Saroj"
text=user.removeprefix("Mr. ")
print(text)
"""Q4. Remove file extension

Given string: "notes.txt"
Apply removesuffix(".txt")

Result: notes"""
user= "notes.txt"
text=user.removesuffix(".txt")
print(text)
"""Q5. Remove both prefix and suffix

Given string: "www.python.org"
Apply removeprefix("www.") and removesuffix(".org")

Result: python"""
user="www.python.org"
text=user.removeprefix("www.")
text_1=user.removesuffix(".org")
print(text,"\n",text_1)
user="www.python.org"
text=user.removeprefix("www.")
text_1=text.removesuffix(".org")
print(text_1)