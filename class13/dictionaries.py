

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?

user_data = {'user_id': 400,
             'fname': 'fritz'}

# print(user_data)

#print(type(user_data))
# Bracket notation - we can grab the value by referencing the key

# print(user_data["fname"])
# print(user_data['user_id'])

# # Add new key/value pair
user_data['adress']  = 'elm street'
# print(user_data)

# lets look at all the methods available to us
#print(type(user_data)

# lets try one
new_dict = dict()
# print(type(new_dict))

# Dict constructor
# user_data = dict(user_id = 400, fname = 'daisy')
# print(user_data)

# Let's update our name key



# Dictionary methods
# Lets use the keys methods to get the keys from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Let's look at our keys
# print(f' the keys for this dog dictionary are {dog.values()}')

# dog_infomation = dog.values

# print(dog_infomation)
# or set it as a variable?



# Lets use the values methods to get the values from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets look at our values
# print(dog)
# dog.clear()
# print(dog)

# or set to a variable

# Lets use clear method to remove all elements

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use get method to get a key value

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# print(dog.get('age'))


# lets look at one of the parameters to show an error if the key doesnt exist

# print(dog.get('temperanemt', 'keys does not exist in dictionary'))


# Lets create a copy

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

new_dog = dog.copy()
dog['breed'] = 'Golden Retriever' #updating a value in our oringinal dictionary

# print(f'original dictionary: {dog}')
# print(f'Copy of original: {new_dog}')


# Lets remove a specified key with pop
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}


# Lets remove a last inserted key-value pair with popitem
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

# age = dog.popitem()
# print(age)

# Get a list with each key-value pair with items
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

key_value_pairs_in_a_list = dog.items()
# print(key_value_pairs_in_a_list)



# we can loop through
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}


    # print(key,value)


# Update dictionary
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

dog.update({'temperment': 'happy'})

# print(dog)

# Update can also update current key value pairs, as well as adding
size = {'size': 'small'} # makes new value
dog.update(size)

dog.update({'size':'medium'}) # updates the pair from small to medium

# print(dog)


# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}

# print(list[3])
# print(dict[3])

list1[3] = 'z'
dict1[3] = 'z'

# print(list1)
# print(dict1)



'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]

dict2 = {}

# for i in range(len(list1)):
#     new_dict.update({list1[i] :list2[i]})
# print(new_dict)



''' Zip Solution

When you use the zip() function in Python, it takes two or more data sets and "zips" them together. This returns an object containing pairs of items derived from the data sets. 
'''

my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# result = dict(zip(my_keys, my_values))
# print(result)



'''
Exercise

Write a dictionary that five countries and their languages Then have your code print the languages of each country one at a time.
Hint: Use the items() method


'''

languages = { 'USA': 'English', 'Mexico': 'Spanish', 'France': 'French', 'Portugal':'Portugese', 'Belgium':'Dutch' }
    


# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small'],
           'region':['central asia', 'south america', 'united states'] }


# print(choices["flavors"][1])

# Lets make a dataframe out of this
#import pandas as pd

# choices_df = pd.DataFrame(choices)
# print(choices_df)


# Lets rename the columns
# rename_choices_dict = {'flavor': 'column1',
#                        'sizes': 'column2',
#                        'region': 'column3'}
# choices_df.rename(columns = rename_choices_dict, inplace= True)
# choices_df.to_csv('output.csv', index = False)
# # print(choices_df)



'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''


'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list

output = {}


# What about the count method for Lists?? 

# for m in my_list_items: # looping thourgh our list
#     if m not in output:
#         output['m'] = 1
#         print(output)
#     else:
#         output['m'] += 1
#         print(output)

# for m in my_list_items:
#     output[m] = my_list_items.count(m)
# print(output)

# from statistics import mode



'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},
           {'name': 'David', 'title': 'developer', 'salary': 65000}]

title_salary_dict= {}

title_count_dict= {}

for r in records:
    # print(r)
    title = r['title']
    salary = r['salary']
    # print(title)
    # print(salary)
    if title not in title_salary_dict:
        title_salary_dict[title]  =salary
        title_count_dict[title] = 1
        # print(title_salary_dict)
        # print(title_count_dict)
    else: 
        title_salary_dict += salary
        title_count_dict += 1
        print(title_salary_dict)
        print(title_count_dict)


import pandas as pd













 



