# 1 concatination property(+):it join the two lists
list_1=[10,50,60]
lst_2=["saroj","rabi","krishna","sushil"]
txt=list_1 + lst_2
print(txt)
# [10, 50, 60, 'saroj', 'rabi', 'krishna', 'sushil']
# indexing:it acess the list element using index number
list_1=[10,50,60]
print(list_1[1])
# 50
# ==slicing
list_1=[10,50,60,"saroj","55.5"]
print(list_1[1:4])
# 50, 60, 'saroj
# ====
list_1=[10,50,60,"saroj",55.5]
text=list_1[-2:]
print(text)
# output['saroj', 55.5]
list_1=[10,50,60,"saroj",55.5]
lst_2=["a","b"]
# [10,50,60,"saroj",55.5,"a","b"]
list_1.append(lst_2)
print(list_1)
list_1=[10,50,60,"saroj",55.5]
lst_2=["a","b"]
print(list_1 + lst_2)
# [10,50,60,"saroj",55.5,"a","b"]
# ====nested_list it can be define as a list inside a list

list_1=[10,50,60,"saroj",55.5]
lst_2=["a","b"]
result=list_1 +[lst_2]
print(result)


