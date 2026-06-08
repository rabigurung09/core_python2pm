# =====keys====
# syntax: var_name.keys()
# 2=====values====
# syntax:var_name.value()
# 3========items======
# syntax:var_name.item()
# 4=====get=====
# syntax:var_name.get("keyvalue")
# 5====update=======
# syntax:var_name.update({key:value})
# 6====clear=====
# syntax:var_name.clear()
# 7=====setdefult=====
# syntax:var_name.setdefult('keyvalue')
# 8=====pop=====
# syntax:var_name.pop("keyvalue")
# 9====popitems=======
# syntax:var_name.popitems()
student = {
    "name" : "saroj",
    1 : "id1",
    55.55 : "weight", #tree_height
    "age" : 25,
    "gender" : "Male",
    "marks" : [20,40,60,80,[2,4,6]],
    
}
# =====keys====
# it gives all key in dictanory
text=student.keys()
print(text)
# output : dict_keys(['name', 1, 55.55, 'age', 'gender', 'marks'])
# 2=====values====
# it gives all the value in dictonary
student = {
    "name" : "saroj",
    1 : "id1",
    55.55 : "weight", #tree_height
    "age" : 25,
    "gender" : "Male",
    "marks" : [20,40,60,80,[2,4,6]],
    
}
print(student.values())
# output:dict_values(['saroj', 'id1', 'weight', 25, 'Male', [20, 40, 60, 80, [2, 4, 6]]])
# 3========items======
# it gives all key value in tuphle formand seprate by comma(,)
print(student.items())
# output : dict_items([('name', 'saroj'), (1, 'id1'), (55.55, 'weight'), ('age', 25), ('gender', 'Male'), ('marks', [20, 40, 60, 80, [2, 4, 6]])])
print(student["age"])
# output: 25
# 4=====get=====
# it access the key value using get mathod /function
print(student.get("name"))
# output: saroj
print(student.get("age"))
# output: 25
print(student.get("adddresh","word not found"))
# ouput :none
# print(student["adddresh"])it gives the error if key not found
# output :word not found
# 5====update=======
# syntax=.update({key:value})
# it update the values of respected key and if found ,if the value is not found it add the value to the distonary
student["name"]='krishna'
print(student)
# output: {'name': 'krishna', 1: 'id1', 55.55: 'weight', 'age': 25, 'gender': 'Male', 'marks': [20, 40, 60, 80, [2, 4, 6]]}
student.update({"name":"rabi"})
print(student)
# output:{'name': 'rabi', 1: 'id1', 55.55: 'weight', 'age': 25, 'gender': 'Male', 'marks': [20, 40, 60, 80, [2, 4, 6]]}
# 6====clear=====
# it removes all the key value of distonary and make i empty
student.clear()
print(student)
output :{}
# 7=====setdefult=====
# if the key is found it show defult value if not found it then it add extar key value 
print(student.setdefault("name"))
student.setdefault("address")
print(student)

# output :{'name': None, 'address': None}
student.setdefault("age","35")
print(student)

# 8=====pop=====
# it removes the key value of dictonary that we select
student.pop("name")
print(student)
# 9====popitems=======
# it remove the last key value of dictonary
student.popitem()
print(student)
# output :{'name': 'rabi', 1: 'id1', 55.55: 'weight', 'age': 25, 'gender': 'Male'}
