#============StringFunction=====================
#A string function is a tool or method that helps to manipulate, modify, or analyze text.
#1.==========Case Conversion:(upper,lower,title,capatilize) =====================
#a. Upper case conversion: it converts all letters into upper case(fully capital)
#syntax:
# variableName.upper()

# #example:
# name = "Saroj"
# text = name.upper()
# print(name.upper())
# print(text)
# print(name)

#b===lowercase: it converts word all letters into lowecase (small albhabetic form)
#syntax:
# variableName.lower()


# collegeName = "xAVIER iNTERNATIONAL cOLLEGE"
# print(collegeName.lower())

#c.title(): it converts every words inside the sting first letter capital and others in small.
#syntax:
# variableName.title()

# colleegName = "xavier international college"
# print(colleegName.title()) #Xavier International College


#d.capatilize():it converts first word first letter capital and others remains in lowercase.
# colleegName = "xavier international college, xavvr int colleGe"
# print(colleegName.capitalize()) #Xavier international college, xavvr int college




#Qn.Write a program to capitalize only the first letter of the string "python is fun".




#2.=======Checking Methods (Return True/False):isalpha,isdigit,isalnum,isspace,islower,isupper========


#In checking method we check the real string type like it may be isdigit(),isalpha(),isalnum(){albhabet+number-->comboo},ispace(),islower(),isupper().
# if match then its output is true otherwise false.
# a = " "
# print(a.isalpha())


#a.========isalpha(): isalpha() checks the string in alphabetic form if alphabetic then active true otherwise false ================
# text = "HelloWorld"
# print(text.isalpha()) #True

# text = "Hello World"
# print(text.isalpha())  #False  it is't take space

# num = "123"
# print(num.isalpha()) #False

# symbol = "@#$%^"
# print(symbol.isalpha())

#==========b. isdigit(): it checks the numerical data. if data is numerical then active(true) otherwise false. it always takes integer value.======
# num = "1234.06"
# print(num.isdigit()) #false

# number = "1234"
# print(number.isdigit())  #True

# number = "-1234"
# print(number.isdigit())  #false


#============c. isalnum(): it checks both alphabet,number or combination of both then, it gives true.===========
#example:
# text = "abc123"
# print(text.isalnum()) #True

# number = "123"
# print(number.isalnum()) #True

# word = "hello"
# print(word.isalnum())   #True

# word = "hello Wordd"
# print(word.isalnum())   #False

# name = "sarojKumar"
# print(name.isalnum()) #True


#==========d. isspace(): isspace() check only space inside stings===========
# a = ""
# print(a.isspace()) #False

# a = " "
# print(a.isspace()) #True

# name = "saroj kumar"
# print(name.isspace())  #False


#========e. islower(): this checks the strings is in lowercase.
#example:
# name = "saroj"
# print(name.islower())  # True

# name1 = "sarOj"
# print(name1.islower())  #False

# ========f. isupper(): it checks all character inside string is in upper case. if yes then it gives true otherwise false
# name =  "Saroj"
# print(name.isupper())  #False

# username = " SAROJ"
# print(username.isupper()) #True

# actor = "salaman"
# print(actor.isupper())  #false





#3.==========Searching Methods(find(),index(),count())=========


#searching methods search the strings character loction using index value.
#indexValue: index value is always start with zero(0).


#a. =============find():it gives the character location in indexing form. if charcter is not found then it return -1=========
# fruit = "apple"
# path = fruit.find("p")
# print(path) # index 1

# fruit = "aooopple"
# path = fruit.find("p")
# print(path) #index 4


# fruit = "apple, banana"
# print(fruit.find("n")) #9

# fruit = "apple, banana"
# print(fruit.find("ae"))  # -1

#b. index():
# address = "kathmandu"
# print(address.index("u"))


#c. count(): it count the total number of searched character inside the String.
# fruits = "banana"
# print(fruits.count("a"))

# address = "savvvetrroojvv"
# print(address.count("v")) #5
# print(address.count("vv")) #2



"""Qn:
1. take the word "Encyclopedia" and check "cl", "C" ,"ed", "de" using find function and write Output
    
2. take the word "Encyclopedia" and check "cl", "C" ,"ed", "de" using index function and write output.
    
3. mssg = "Hello This is Deepak From Mahendranager" 
count: a, e, m, t ,o

"""




#4.=========Splitting & Joining =======================


#1.spilt():it breaks the strings and converts into list.
# #example:
# name = "saroj"
# print(name.split("s"))      #['', 'aroj']
# print(name.split("a"))      #['s', 'roj']
# print(name.split("r"))      #['sa', 'oj']
# print(name.split("o"))      #['sar', 'j']
# print(name.split("j"))      #['saro', '']



# address = "kkkkathmmmmanduu"

#2.join(): it joins two list and convert it into string. 
# lst1 = ["saroj","bardibas"]
# lst2 = ["sushil", "kathmandu"]
# lst = lst1 + lst2
# result = " ".join(lst)
# print(result)
# print(type(result))

# fruit = ["apple", "Banana"]
# fruit1 = ["orange", "Guava"]
# lst = fruit + fruit1
# print(lst)
# result =",".join(lst)
# print(result)



#5. ================removing space=================
#it removes the unwanted space in string.
#a.strip():it removes the unwanted space from both left and right sides of the string
# name = "    saroj    "
# print(name.strip())


#b. rstrip():it removes the left sides unwanted space from string.
# name = "    saroj    "
# print(name.rstrip()) #    saroj

#c. lstrip(): it removes the unwanted space  from  right side of string.
# name = "    saroj    "
# print(name.lstrip()) #saroj    


#6.==========Alignment Functions==================
#a.======== center(width)===============
#it provides the equal spaces inside both sides of the string.Example if center (20) then it provides 10 (width) 
# from left and 10 (width) from right.
# fruit = "banana"
# txt = fruit.center(20)
# print(txt, "is my favorite fruit.")


# #b. ljust():it provides the space from right to the strings
# fruit = "banana"
# txt = fruit.ljust(20)
# print(len(fruit))
# print(len(txt))
# print(txt, "is my favorite fruit.")



#c. rjust: it provides the space from left side of the string.
# fruit = "banana"
# txt = fruit.rjust(20)
# print(txt, "is my favorite fruit.")



#7.========Starts & Ends================
#a. strtswith(): it checks the string starting character.if match then gives true otherwise false.
# name = "saroj"
# print(name.startswith("s")) #output:True
# print(name.startswith("j")) #output:False


# #b. endswith(): it checks the string ending character.if match then gives true otherwise false.
# print(name.endswith("s"))   #output:False
# print(name.endswith("j"))   #output:True



#8.length(): it finds the actual length of string.
# fruits = "banana"
# print(len(fruits)) #output: 6



#9.=========== remove suffix/prefix===============
#it removes suffix and prefix from the string.

# email = "admin.@gmail.com"
# print(email.removeprefix("admin."))
# print(email.removesuffix(".com"))


# email = "admin.@gmail.com.saroj"
# print(email.removeprefix("admin."))
# print(email.removesuffix(".com"))

# email = "admin@gmail.com.saroj"
# print(email.removeprefix("admin"))
# print(email.removesuffix(".com.saroj"))


#10===replace() function:  it replace the each and every character of the strings or as a whole string.
#example:
# name = "saroj"
# print(name.replace("s","T"))  #Taroj
# print(name.replace("saroj", "krishna"))  #krishna



