"""tuple:
    collection of data(elements or data items)which is immutable, ordered and allows duplicate element
    tuple is generally create dby small bracket()but it optional and element of tuple are seprated by comma
    for example
    a=5,
    we can store different data type together in a tuple
    for example
    details=(1,"saroj",26,"60.55","kathamandu",True)
    """
# =======creating tuple=====
mytuple=()
mytuple=tuple()
print(mytuple)
# ()
# details=(1,"saroj",26,"60.55","kathamandu",True)
# details[1]="RABI"
# print(details)
# we cannot change value in tuple.it throws "tuple"object does not support iems assignment "error"
# ===============concation(+)=======
fruits=("apple","orange","pineapple")
color=("red","orange","yellow")
print(fruits + color)
# output:('apple', 'orange', 'pineapple', 'red', 'orange', 'yellow')
print(fruits[1])
# excess value of tuple
# output :orange
# ======slicing====
# syntax:
# var_name[start:end:step]
print(fruits[::2])
# :output:('apple', 'pineapple')
print(fruits[-1])
# :output:pineapple
comboo=('apple','orange','pineapple','red','orange','yellow','ram','gita')
print(comboo[-4:-1])
# orange yellow ram
print(comboo[-2])
# =====methods in tuple===
# .count()
comboo=('apple','orange','pineapple','red','orange','yellow','ram','gita')
print(comboo.count('orange'))
# output:2

# .index():it gives the index of search value

comboo=('apple','orange','pineapple','red','orange','yellow','ram','gita')
print(comboo.index('orange'))
# output:1


student={
    "name":"saroj",
    1:"id1",
    55.5:"weight",
    "age":25,
    "gender":"male",
    "marks":(20,40,60)
}
txt=student.get("marks")
print(txt)
txt_1=list(txt)
print(txt_1)
txt_1.append(1)
print(txt_1)
txt_2=txt_1
txt_2=tuple(txt_2)
print(txt_2)
# output:(20, 40, 60)
# [20, 40, 60]
# [20, 40, 60, 1]
# (20, 40, 60, 1)
a=[5,4]
print(tuple(a))
# (5, 4)
a="apple"
b="banana"
sep=a
a=b
b=sep
print(a,b)
print(f"a is {a}\n b is {b}",sep="")
# output:banana apple
# a is banana
#  b is apple
# ========unpack tuple =====
# it assign the values of tuphle in different variable in a single statement
a,b,c=(2,1,5)
print(a)
print(b)
print(c)
# output:2
# 1
# 5
# a,b,c=(2,1,5,4)
print(a)
print(b)
print(c)
# output:  a,b,c=(2,1,5,4)
#     ^^^^^
# ValueError: too many values to unpack (expected 3, got 4)
a,b,*c=(2,1,5,4)#it takes all the values in the tuphle and makes all the remaning value in list
print(a)
print(b)
print(c)
# output:2
# 1
# [5, 4]