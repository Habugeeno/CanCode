'''
Ranges
    - Must be integers, whole numbers
    - Used to iterate
    - Does not store all the numbers, but knows what they should be
    - Simple to write and create
    -saves memory
'''

# Using the range function, lets count to 20

# tom = range(21)

# for t in tom:
#     print(t, end= ' ')


# ''' Let's try these '''

# for l in range(16, 2, -3):
#     print(1+1, sep= ', ')

# for r in range(3,2):
#     print(r)




'''
Write a range that is every five years from 1960 to 2000.
'''

# five_years = range( 1960, 2001, 5)

# for s in five_years:
#     print(s)

'''
range(start, stop, step)
'''






'''
Write a range that counts down from 30 to 0
'''

# gexs = range(30, -1, -1)

# for g in gexs:
#     print(g, end= ' ')

# lames = reversed(range(0, 11))

# for o in lames:
#     print(o, end= " ")


'''
Exercise
Rewrite the for loop we made last class that goes through a list and prints each item in the list, along with its index. (Hint: you can use a range, and you won't need a separate counter variable.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars
'''

planets = ["mercury", "venus", "earth", "mars"]
output += f' {p}: {planets[p]})'



    


''' Exercise
You have a list of employees, and a list of job titles. Assume the lists are the same length and in the same order.
Use one for loop to go through both lists and print the job title of each employee.
For example, if these are your lists:
employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']
This should be your output:
Bob's job title is accountant.
Cynthia's job title is engineer.
Abdul's job title is recruiter.

'''


employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']



'''
Write some code that creates a range based on what the user enters. 
Challenge: you can make a range with 1, 2, or 3 numbers. How would you allow the user to pick any of these options?
'''
