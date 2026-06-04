list=[1,2,3,4,9,5,67,67,54,454]
list.append(555)
list.append("ram")
print(list)
# output:[1, 2, 3, 4, 9, 5, 67, 67, 54, 454, 555, 'ram']
list=[1,2,3,4,5]
list_2=[6,7,8,9,10]
list.extend(list_2)
print(list)
# output:[1,2,3,4,5,6,7,8,9,10]
list=["ram","shyam","hari","ram"]
list.remove("ram")
print(list)
# output:['shyam','hari','ram']
list=["rabi","neymar","romanring"]
list.pop(2)
print(list)
list=[1,3,4,56,6,6,6,]
list.sort()
print(list)
# output:[1, 3, 4, 6, 6, 6, 56]
list=[1,3,4,56,6,6,6,]
list.reverse()
print(list)
# output:[6, 6, 6, 56, 4, 3, 1]
list=[1,3,4,56,6,6,6,]
list.sort(reverse=True)
print(list)
# output:[56, 6, 6, 6, 4, 3, 1]
list=["ram","shyam","rabi"]
list.copy()
print(list)
# output:['ram', 'shyam', 'rabi']
list=["pen","pencil"]
list.clear()
print(list)
# output:[]
list=["hary","era","hary"]
list.count("hary")
print(list)
# ['hary', 'era', 'hary']
list=["hary","era","hary"]
list.insert(0,"ram")
print(list)
# output:['ram', 'hary', 'era', 'hary']
