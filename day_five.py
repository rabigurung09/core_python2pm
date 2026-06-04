# ====case_conversation method====
p_n="hello world"
print(p_n.upper())
# HELLO WORLD
programing_l="PYTHON PROGRAMING"
print(programing_l.lower())
# python programing
s="hello world"
print(s.capitalize())
# Hello world
# Q4.Differentiate between title() and capitalize() with example.
"""
     difference between title and capitalizer is that capatilizer only capitalize the first 
word of value while making all word small and title makes the value of first word of every value capitalize
    """

name="rabi gurung"
print(name.title()) 
# Rabi Gurung
name_1="rabindra"
print(name_1.capitalize())
# Rabindra
# Q5.Write a program to capitalize only the first letter of the string "python is fun".
pro_name="python is fun"
print(pro_name.capitalize())
# Python is fun
# Q6.What will be the output?
s = "hELLO wORLD"
print(s.capitalize())
# Hello world
"""
Q7.Write a program to take user input as (name,collegeName,address,favouritePlayer,FavouriteGame) and convert it into:
    •	uppercase 
    •	lowercase 
    
    """
user_1=input("Enter your college name=")
user_2=input("Enter your address=")
user_3=input("Enter your favourateplayer=")
user_4=input("Enter your favourategame=")
print(user_1.upper())
print(user_2.upper())
print(user_3.upper())
print(user_4.upper())
# UNIVERSAL
# BHAKTAPUR
# NEMAR
# FOOTBALL
"""Q8.What will be the output?
    s = "123abc"
    print(s.upper())"""
s = "123abc"
print(s.upper())
# 123ABC
"""Q9.Correct the following string using proper case (title case):
    s = "welcome to nepal"
    """
s="welcome to nepal"
print(s.title())
# Welcome To Nepal
# Q10.Predict the output:
"""    s = "python programming"
    print(s.capitalize())
    print(s.title())
"""
# Python programing
# Python Programing
player=[input("enter yor fav player")]
player_2=input("enter yor fav player")
player_3=input("enter yor fav player")
player.append(player_2)
player.append(player_3)
print(player)




text = "saroj  ram"
print(text.split())   #it converts string into list
print(list(text))   #it converts the every character of string into list. 
user=input("enter your fav player").split()
user_1=input("enter your fav player")
user_2=input("enter your fav player")
user.append(user_1)
user.append(user_2)
print(user)
# ['messi', 'nemar', 'ro']
# 
"""Write a Python program that:

Takes a sentence from the user.
Takes a word to search.
Uses only:
find()
index()"""


