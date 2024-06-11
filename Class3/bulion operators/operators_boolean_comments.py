# Operators, Boolean Expersion and Comments

# A Comment
temprature = 95 # This is a inline comment

# An standard single line comment 
first_name_2 = 'tommy' ''' This is a Multi line comment - inline comment'''
last_name_2 = 'the train' """inline comment witrh dounle quotes"""

'''
everything between the qutoes will be commented out
'''

# Comment me (The perimeter of a rectangle)
# length = 5 # The inputs 
# width = 7

# perimeter = 2 * (length + width) # the formula 

# print(perimeter) # The Output


'''Creating a fahrenheit to celsius calcualtor '''

fahrenheit = 89 # The Input

celseius = (fahrenheit - 32) * 5 / 9 # The formula

# print(celseius) # The output



'''short cut operators'''
# Add 5 to me 
age = 25

age += 5 # Adding 5 via shortcut operators

# print(age)

# Add ten years 
year = 2024

year += 10

# print(year)

# Subtract 20
num_one = 55

num_one -= 20 

# print (num_one)

# Subtract 15
num_two = 11

num_two -= 15

# print(num_two)

# Multiply by 3
my_value = 9

my_value *= 3

# print(my_value)

# Multiply by 10
mileage = 15

mileage *= 10

# print(mileage)

# Divide by 2 / 
pizza_slices = 8

pizza_slices /= 2

# print(pizza_slices)

# Divide by 7 /
fees = 8.90

fees /= 7 

# print(fees)


'''' Exponents'''
# raise to the 3rd power **
num_three = 6

num_three **= 3

# print(num_three)

# raise top the second power **
val_one = 16

val_one **= 2

# print(val_one)

# INterger division, how many times does 3 goes into 16 //
data = 16

data //= 3

# print(data)

# Interger divide by 4 //
point = 9

point //= 4

# print(point)



'''Moudulus we use often to find if a value is odd or even'''
# Find the remainder id divided by 3 % 
val_three = 10 

val_three %= 3

# print(val_three)

# find the remander if divided by 5 %
val_four = 14

val_four %= 5

# print(val_four)

# Refactor me 

'''
fahrenheit = 89 

celseius = (fahrenheit - 32) * 5 / 9
'''


fahrenheit -= 32 # perenthesis

fahrenheit *= 5/9

celseius = fahrenheit

# print(celseius)


''' Boolean Operators '''

# Is 7 less than 5? < 
# print(7 < 5) 

result = (7 < 5) 

print(f"Is 7 less than 5? {result}")

# Is 4 less than or equal to 4? <=
# print(4 <= 4) 

pock = (4 <= 4)

# print("is 4 less than equal to 4?", pock)

# is 5 equal to 5? ==

game = (5 == 5)

# print("is 5 equal to 5?", game)

#is 5 greater than or equal to 6? >=

lick = (5 >= 5)

# print("is 5 greater than or equal to 6?", lick)

#is 6 greater than 2? >

nose = (6 > 2)

# print("is 6 greater than 2?", nose) 

# is 100 not equal to 75? !=

lame = (100 != 75)

# print( "is 100 not equal to 75?", lame)

# print(5 == 5 and 4 == 4) #true 
# print(2 == 2 and 3 == 3) #true
# print(1 == 2 and 2 == 10) #false

log_1 = (5 == 3)

log_2 = (4 == 7)

# print('log 1', log_1)

# print('log 2', log_2)

# print('log 1 and log 2', log_1 and log_2)

# or 
# print(5 == 5 or 5 == 2) # True if one is true


# not 
is_it_autumn = True

# print(not is_it_autumn)

# is x less than y
x= 11

y= 10

# print(x < y)

# Are we the same 
fname = "mike"

first_name = "mike"

# print(fname is first_name)

# in

# print('j' in 'january')

# print('f' in 'march')

# fromated srting
pet= 'dog' # My variable is to be used in my formated string

print(f'I own a {pet}')






''' 
The program that calculates the area of the triagle (HW)
'''

# area of a trangle = 1/2