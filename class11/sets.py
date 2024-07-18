'''
Fun Facts about Sets

-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. You can still loop through a set with a for loop.

'''

# Ways to create a set
i_am_empty = set()
new_dic = dict() # this would be an empty dictionary
# print(i_am_empty)

# What am I?
check_my_type = ()
# print(type(check_my_type))

# Pass in a list, they lose their order
my_fav_colors_list = ['green', 'blue', 'red']
my_fav_color_set = set(my_fav_colors_list)
# print(my_fav_color_set)

# # Unordered
my_unordered_set = {'blue', 'green', 'red', 'orange'}

# Unchangeable
my_unchangeable_set = {'hello', 'welcome', 'to', 'newyork'}
# my_unchangeable_set[3] = 'new jeresy' #note the error

# # Unindexed
my_unindexable_set = {'I', 'cant', 'be', 'indexed'}
# my_unindexable_set[2]
# print(my_unindexable_set[2])

# Break up a string, removes duplicates
word = set('abracadabra')
# print(word)



# Please remove thse duplicates by passing it into a new set named, my_unique_cars
my_cars = ['chevy', 'toyota', 'ford', 'ford', 'honda', 'honda']
# 

# No duplicates - How did we solve this problem before?

'''
8. Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
'''
''' With a for loop and appending'''

#original list
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

# # this will capture our unique states
states_no_duplicates = list(set(states))

# #we will loop through states_backup, and append only the first occurence of each state into
# for s in states:
#     if s not in states_no_duplicates:
#         states_no_duplicates.append(s)
# print(states_no_duplicates)

''' With sets and returning a list '''

# states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']


# We can loop through sets
top_ten_movies = {'shawshank redemption', 'avatar', 'avengers', 'its a wonderful life'}



# Let's add silver .add()
colors = {'blue', 'green', 'red'}
colors.add('SILVER')
# print(colors)
# Lets clear all our items .clear()
# transportation = {'cars', 'bikes', 'plane'}


# Lets create a copy .copy()
sitcoms = {'friends', 'seinfeld', 'honeymooners'}
comedy = sitcoms.copy()


# Let's add to sitcome to confirm we have a copy
sitcoms.add('In Living Color')

# print(sitcoms)
# print(comedy)



# Remove vermont from our set
states = {'california', 'new york', 'vermont', 'connecticut'}
states.remove('vermont')

# print(states)


# Difference - What's different?
student_set = {'brad', 'dez', 'kenneth'}
student_set_2 = {'brad', 'dez', 'chelsea'}
result = student_set - student_set_2 # operator
result = student_set.difference(student_set_2) #method

# print(result)


# Intersect - What do we have in common? '&'
my_schedule = {'mon', 'wed', 'thurs'}
pats_schedule = {'wed', 'fri', 'sat'}

same = my_schedule & pats_schedule
same = my_schedule.intersection(pats_schedule)

# print(same)

# Union - All pets that appear in any set .union
joel_pets = {'dog', 'cat', 'bird'}
mustafa_pets = {'chickens', 'dog', 'fish'}
sarah_pets = {'bird', 'dog', 'fish'}
leah_pets = {'turtle'}

all_pets = joel_pets.union(mustafa_pets, sarah_pets, leah_pets)
all_pets = joel_pets | mustafa_pets | sarah_pets | leah_pets

# print(all_pets)


# Symmetric difference - Items outside of matching items ^ .symmetric_diffrence 

wendy_books = {'catcher in the rye', 'richest man in babylon'}
cain_books = {'catcher in the rye', 'richest man in babylon', 'sounder'}

# look = wendy_books.symmetric_difference(cain_books)
look = wendy_books^cain_books

# print(look)

'''
Exercise - Sets
You work for a sales company and must generate a set of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a set of customers over 60, and a set of customers who have made at least 5 purchases. Use a set operation to output a set of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
Output: {'Dominic', 'Simone'}
'''

# solved with intersection - solve with 1 or 2 lines of code
# over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
# over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
# customer_discount = over_60_years.intersection(over_5_purchases)
# print(customer_discount)


'''
Exercise - Sets
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''
''' Our variables '''
#data collection  sets
python, js = set(), set()

#inputs
dev_type_input, dev_name_input = ' ', ' '

msgs = ('invalid input please try again', 'thank you have a nice day')
invalid_input = msgs[0]
have_a_nice_day = msgs[1]

# User Instructions
\
while True:
    dev_type_input = input('type p for Python Dev, js for javascript, or Stop to Exit the program: ').casefold()
    if dev_type_input == 'stop':
        print(have_a_nice_day)
        break
    if dev_type_input == 'p' or dev_type_input == 'js': # get a name and offer an exit
        dev_name_input = input('please enter developer name: ').casefold()
        if dev_name_input == 'stop':
            print(have_a_nice_day)
            break
        elif dev_type_input == 'p':
            python.add(dev_name_input.title())
            print(python)
        elif dev_type_input == 'js':
            js.add(dev_name_input.title())
            print(js)
    else:
        print(invalid_input)

know_both = python.intersection(js)

know_js_not_python = js.difference(python)

know_js_or_python_not_both = js.symmetric_difference(python)

print(f'''{know_both} know's both ''')

print(f''' {know_js_not_python} know's javascript not python''')

print(f'''{know_js_or_python_not_both} know's python or javascript''')
