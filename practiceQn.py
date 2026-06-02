"""
1. WAP to find the area of a parallelogram by taking input from user
Keynotes:
Input: base, height
Formula: area = base * height
Same as rectangle concept but different shape name


2. WAP to find the perimeter of a square by taking input from user
Keynotes:
Input: side
Formula: perimeter = 4 * side
Single input, multiplication only

3. WAP to find the simple interest by taking input from user
Keynotes:
Input: principal, rate, time
Formula: SI = (P * R * T) / 100
Watch division carefully

4. WAP to find the average of 3 numbers by taking input from user
Keynotes:
Input: num1, num2, num3
Formula: avg = (n1 + n2 + n3) / 3
Addition + division

5. WAP to convert kilometers to meters by taking input from user
Keynotes:
Input: kilometers
Formula: meters = km * 1000
Simple unit conversion, multiplication only

"""
# 1
# base=int(input("Enter the base of parallelogram"))
# height=int(input("Enter the  height of parallelogram"))
# area =base*height
# print("the area of parallelogram is ",area)
# 2
# side=int(input("Enter the side of square"))
# parameter=4 * side
# print(parameter)
# 3
# principal=int(input("Enter the principal of interest:"))
# rate=int(input("Enter the rate of interest :"))
# time=int(input("Enter the time of interest:"))
# interest= principal*rate*time
# print(interest)
# 4
# num1=int(input("enter one number"))
# num2=int(input("enter second number"))
# num3=int(input("Enter third number"))
# average=(num1 +num2 +num3)/3
# print(average)
# 5
kilometer=int(input("Enter the distance u cover in bike"))
meter=kilometer*1000
print(meter)


# rows = 5

# for i in range(1, rows + 1):
#     spaces = " " * (rows - i)
#     stars = "*" * (2 * i - 1)
    
#     print(spaces + stars)

# Simple Interest Program


# principal = float(input("Enter Principal Amount (P): "))
# rate = float(input("Enter Rate of Interest (R): "))
# time = int(input("Enter Time (T in years): "))
# si = (principal * rate * time) / 100
# print("Simple Interest is:", si)

#take any numeric data from user in string format and convert it into integer like age, price , account_no:





age = input("Enter age: ")
print(age)
print(type(age))
