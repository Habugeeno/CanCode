# Let's talk about the print statement
# This is a comment, Use The Pound Sign
# Ctrl / a highlighted line to comment the higlighted section
# Ctrl Z to undo code
# [] are list, {} dictonary
'''
this is a multi line comment
this can go on another line 
this won't print lines
'''


# print ('hello world') # Print Built in Function


# Addition (interger data type)

# print(4+2) 
# print (7+10)
# print(100+200)

# Subtration (interger data type)

#print(10 - 7)
#print(4 - 3)
#print(9 - 8)

#Multiplication 

# print(4 * 8)
# print(3 * 9)
# print(11 * 9)

# Division  (interger data type) (/ is for the full exponent // is a rounded exponent)

# print(10 // 3)
# print(5 // 2)
# print(4 / 3)

# Try Except

#  try:
#     print(5 / 0)
# except ZeroDivisionError as e: 
#     print("You can't divide by 0, Idiot")

# Exponents (This flsahes the coods from the line you print)

# print(5 ** 5)
# print(2 ** 5)
# print(3 ** 6)

# Modulo / Mod / Remainder (finding out if num is odd or even)
# print(5 % 2)
# print(10 % 4)
# print(6 % 2)

# Using variables as placeolders 
#This is assing int value 1 to variable num_one (= is the operatort assigner)
num_one = 1 
num_two = 20

# print(num_one + num_two)


# Program to find the perimeter of a rectangle
# perimeter = 2 * (length + width)

# declaring your variables
length = 10 
width = 7

perimeter = 2 * (length + width)

# print('The perimeter of my rectangle is', perimeter)


# INterger 
num_3 = 5  # declare variable
# print(num_3) # print variable vaule
# print(type(num_3)) # we can check the data type 

# String 
fav_color = "destroy lonely if looks can kill blue"
# print(fav_color)
# print(type(fav_color))

#Boolean
technical_fault = False
# print(technical_fault)
# print(type(technical_fault))

# Float 
num_4 = 4.05
# print(num_4)
# print(type(num_4))

# List 
student_grades = [100, 95, 70, 85, 40]
# print(student_grades)
# print(type(student_grades))

# For loop
# for p in student_grades:
#     print('one grade is ', p)

# dictionaries
demographic_info = {'first name' : "Joe",
                    'last name' : "Smith",
                    'State' : "NY"}

# print(demographic_info)
# print(type(demographic_info))

# Casting 
# When you get input from a user, Python will make it a string

my_string = '5' # variable is a string of num 5
# print(my_string)
# print(type(my_string))

#changing the data type from string to int
new_number = int(my_string) # casting our string '5' to a interger
# print(new_number)
# print(type(new_number))

# casting an interger to a string 
# second_numb = 10 
# print(type(second_numb))
# print(second_numb)

# new_string = str(second_numb)
# print(type(new_string))
# print(new_string)

# Colors 
best_colors = ['blue', "black", 'red', 'yellow']

# len_counts_items = len(best_colors) # we are passing the argumentbest_colors into len function
# print(len_counts_items)

one_color = 'orange'
# my_count = len(one_color)
# print(my_count)

# for o in one_color:
#     print(o)

# Eval
cold_weather = 'True'
# print(eval(cold_weather))

# Find the perimeter of a triangle
# perimeter = side_one + base + side_two
# User has a triangle of a 

side_one = 6 
sied_two = 7
base = 4

# perimeter_2 = (side_one + base + sied_two)
# print(perimeter_2)

# Temprature Code
f = 76 

c = ((f - 32) * 5 / 9)
# print(c)
