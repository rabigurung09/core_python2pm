# # ====extend():
# # example
# # lst1=[1,2,3]
# # lst2=[5,6,7]
# # lst1.extend(lst2)
# # print(lst1)
# # 2remove():it remove the value of list
# # num_list=[10,50,60,80,90,50,20,30]
# # num_list.remove(10)
# # print(num_list)
# num_list=[10,50,60,80,90,50,20,30]
# num_list.remove(90)
# print(num_list)
# # 3 pop()it removes the value using indexnumber
# # varable_name.pop(indexnumber)
# # example
# num_list[10,50,60,80,90,50,20,30]
# num_list.pop(4)
# print(num_list)
# # extend():it add the one list value into another extended list
# list_1=[1,2,3]
# list_2=[4,5,6]
# list_1.extend(list_2)
# print(list_1)
# # ===clear():it clear the list all element value
# syntax
# # var_name.clear()
# num_list=[10,50,60,80,90,50,20,30]
# num_list.clear()
# print(num_list)
# fruit_list=["apple","banana"]
# fruit_list.clear()
# print(fruit_list)
# ===count: it count the number of search value
# num_list=[10,20,30,30,30]
# print(num_list.count(20))
# num_list.count(20)
# num_list=[10,50,60,80,90,50,20]
# print(num_list.count(50))
# ====insert() it insert the value in provided index number 
# syntax:variable.insert(indexvalue ,insertvalue)"""parameter"""
num_list=[10,50,60,80,90,50,20]
num_list.insert(5,99)
print(num_list)
# [10, 50, 60, 80, 90, 99, 50, 20]
# sort:it arrange the element in accending order
# syntax:variable.sort()
num_list=[10,50,60,80,90,50,20,30,40]
num_list.sort()
num_list.sort(reverse=True)
print(num_list)
# [10, 20, 30, 40, 50, 50, 60, 80, 90]
# [90, 80, 60, 50, 50, 40, 30, 20, 10]
# reverse :it arrange the value of variable in reverse
num_list=[10,50,60,80,90,50,20,30,40]
num_list.reverse()
print(num_list)
# [40, 30, 20, 50, 90, 80, 60, 50, 10]
# copy: it duplicate the value
num_list=[10,50,60,80,90,50,20,30,40]
num_list.copy()
print(num_list)
# [10, 50, 60, 80, 90, 50, 20, 30, 40]

# write a program to add your 3 favourate player in a list using append()function
# note:take 3 favourate players as a input user
list_11=["ram","shyam","hari"]
print(list_11)
user=input("Enter your favourate player")
user1=input("Enter your favourate player")
user2=input("Enter your favourate player")
list_11.append(user)
list_11.append(user1)
list_11.append(user2)git
print(list_11)







