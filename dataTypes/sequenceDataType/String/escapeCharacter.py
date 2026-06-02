# #Escape character: in python escape character is a special type of character which have their own special function/task and start with backslash.
# # ======1.\n=================
# #\n: it breaks the line and switch to next.
# # it only work for string.
# #example:
# print("College\nname ") 
# """ backslash n switch to next line(Output)
# College 
# name 
# """
# print(5,"\n", 3, sep="")  # sep="" it removes extra space
# """Output:print in one line vertically {
#             5              
#             3             
                            
# }"""
# print(5,6,8,sep="+") #Output:5+6+8

# #=========== 2. carriage retun (\r)==========
# #Carriage return: It moves the cursor to the beginning of the same line without moving to the next line.

# print("Hel\ro")  #oel
# print("stud\rent") #entd
# print("College\rName") #Nameege
# print("abcd\r123")  #123d

# print("Develop\rment") # mentlop

# print("12589\rram")
# print("sajha\rTech")
# print("lap\rtop")
# print("univer\rsity")

# ===3. \t (tab)=====:     # \t provides horizontal tab space
# print("hel\to")
print("12589\tram")
# print("sajha\tTech")
# print("lap\ttop")
# print("univer\tsity")

#====4.\v vertical space: vertical tab / vertical spacing
# print("He\vllo")
# print("12589\vram")
# print("sajha\vTech")
# print("lap\vtop")
# print("univer\vsity")

#======\b(backspace):it removes the last character before \b.
# print("univer\b1") #unive1
# print("He\bllo") #Hllo
# print("Hexxxl\blo") # hexxxlo






# a = 5
# b =4
# c =3
# d =8
# print(a,b,c,d, sep="-")
print('It\'s my laptop')