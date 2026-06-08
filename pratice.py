"""List Function Complete Questions.
1. ====================append()===================
1. Create an empty list and append the number 10.
2. Append 20 and 30 to the list [10].
3. Append "Python" to the list ["Java", "C++"].
4. Append the value 50 to [10, 20, 30, 40].
5. Append the list [4, 5] to [1, 2, 3]."""

list=[]
text=list.append(10)
print(list)
list.append(20)
print(list)
list.append(30)
print(list)

list=['python']
list.append('java')
list.append('c++')
print(list)
list=[50]
list.append(10)
list.append(20)
list.append(30)
list.append(40)
print(list)
list=[1,2,3]
list.append(4)
list.append(5)
print(list)
"""2. ====================insert()====================
1. Insert 100 at index 0 in [10, 20, 30].
2. Insert "Apple" at index 1 in ["Mango", "Orange"].
3. Insert 50 before 60 in [20, 40, 60, 80].
4. Insert 999 at the end of [10, 20, 30].
5. Insert "Python" at index 2 in ["C", "Java", "C++"]."""
list=[10, 20, 30]
list.insert(0,100)
print(list)
list=["mango","orange"]
list.insert(1,"apple")
print(list)
list=[20, 40, 60, 80]
list.insert(2,50)
print(list)
list=[10, 20, 30]
list.insert(3,999)
print(list)
list=["C", "Java", "C++"]
list.insert(2,"python")
print(list)
"""3. ==================remove()====================
1. Remove "red" from ["red", "blue", "green"].
2. Remove the number 25 from [10, 25, 30, 40].
3. Remove the first occurrence of 10 from [10, 20, 10, 30].
4. Remove 40 from [10, 20, 30, 40, 50].
5. Remove "banana" from ["apple", "banana", "orange"]."""
list=["red", "blue", "green"]
list.remove("red")
print(list)
list=[10, 25, 30, 40]
list.remove(25)
print(list)
list=[10, 20, 10, 30]
list.remove(10)
print(list)
list=[10, 20, 30, 40, 50]
list.remove(40)
print(list)
list=["apple", "banana", "orange"]
list.remove("banana")
print(list)
"""4.=================== pop()========================
1. Remove the last element from [1, 2, 3, 4].
2. Pop the element at index 2 from [10, 20, 30, 40].
3. Store the popped element in a variable and print it.
4. Pop the first element from [100, 200, 300].
5. Pop the last two elements one by one from [1, 2, 3, 4, 5]."""
list=[1, 2, 3, 4]
list.pop(-1)
print(list)
list=[10, 20, 30, 40]
list.pop(2)
print(list)
list=[1, 2, 3, 4]
text=list.pop(-1)
print(text)
list=[100, 200, 300]
list.pop(1)
print(list)
list=[1, 2, 3, 4, 5]
list.pop(-1)
print(list)
list.pop(-1)
print(list)
"""5. =================extend()========================

1. Extend [1, 2, 3] with [4, 5, 6].
2. Extend ["Apple", "Banana"] with ["Orange", "Mango"].
3. Extend a list with the tuple (7, 8, 9).
4. Combine [1, 2] and [3, 4] using extend().
5. Extend [10, 20] with [30, 40, 50]."""
list_1=[1, 2, 3]
list_2=[4, 5, 6]
list_1.extend(list_2)
print(list_1)
list_1=["Apple", "Banana"]
list_2=["Orange", "Mango"]
list_1.extend(list_2)
print(list_1)
list_1=["Apple", "Banana"]
list_2=(7, 8, 9)
list_1.extend(list_2)
print(list_1)
# 4
list=[1, 2]
list_1=[3, 4]
list.extend(list_1)
print(list)
# [1, 2, 3, 4]
# 5
list=[10, 20]
list_1=[30, 40, 50]
list.extend(list_1)
print(list)
# [10, 20, 30, 40, 50]
"""6. =================sort()=========================
1. Sort [50, 20, 40, 10] in ascending order.
2. Sort [5, 1, 3, 2, 4].
3. Sort ["Banana", "Apple", "Orange"] alphabetically.
4. Sort [100, 50, 200, 25].
5. Sort [3, 3, 1, 2, 1]."""
# 1
list=[50, 20, 40, 10] 
list.sort()
print(list)
# [10, 20, 40, 50]
# 2
list=[5, 1, 3, 2, 4]
list.sort()
print(list)
# [1, 2, 3, 4, 5]
# 3
list=["Banana", "Apple", "Orange"]
list.sort()
print(list)
# ['Apple', 'Banana', 'Orange']
# 4
list=[100, 50, 200, 25]
list.sort()
print(list)
# [25, 50, 100, 200]
# 5
list=[3, 3, 1, 2, 1]
list.sort()
print(list)
# [1, 1, 2, 3, 3]
"""7. ===============reverse()==========================
1. Reverse [10, 20, 30, 40].
2. Reverse ["Apple", "Banana", "Orange"].
3. Reverse [1, 2, 3, 4, 5].
4. Reverse a sorted list [10, 20, 30, 40, 50].
5. Reverse ["Python", "Java", "C++"]."""
# 1
list=[10, 20, 30, 40]
list.reverse()
print(list)
# [40, 30, 20, 10]
# 2
list=["Apple", "Banana", "Orange"]
list.reverse()
print(list)
# ['Orange', 'Banana', 'Apple']
# 3
list=[1, 2, 3, 4, 5]
list.reverse()
print(list)
# [5, 4, 3, 2, 1]
# 4
list=[10, 20, 30, 40, 50]
list.reverse()
print(list)
# [50, 40, 30, 20, 10]
# 5
list=["Python", "Java", "C++"]
list.reverse()
print(list)
# ['C++', 'Java', 'Python']
"""8.=============== count()============================
1. Count occurrences of 5 in [5, 1, 5, 2, 5].
2. Count how many times "Python" appears in ["Python", "Java", "Python"].
3. Count occurrences of "a" in ["a", "b", "a", "c", "a"].
4. Count the number of 10s in [10, 20, 10, 30, 10].
5. Count occurrences of "apple" in ["apple", "banana", "apple"]."""
# 1
list=[5, 1, 5, 2, 5]
print(list.count(5))
# output:3
# 2
list=["Python", "Java", "Python"]
print(list.count("Python"))
#output: 2
# 3
list=["a", "b", "a", "c", "a"]
print(list.count("a"))
# output:3
# 4
list=[10, 20, 10, 30, 10]
print(list.count(10))
# output:3
# 5
list=["apple", "banana", "apple"]
print(list.count("apple"))
# output:2
"""9. ====================index()=======================
1. Find the index of 30 in [10, 20, 30, 40].
2. Find the position of "banana" in ["apple", "banana", "orange"].

3. Find the first occurrence of 5 in [5, 2, 5, 7].
4. Find the index of "Python" in ["Java", "Python", "C++"].
5. Find the position of 100 in [50, 100, 150]."""
# 1
list= [5, 2, 5, 7]
# output:
# output:
# output:
# output:
# output: