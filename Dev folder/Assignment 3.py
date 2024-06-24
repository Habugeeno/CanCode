'''
Email Reader 

Assignment 2: Valid Email, I'm writing a function to check if the inputed email is an valid address

'''

# First the Input 

user_email = input(f'Please enter your email address for weekly subscriptions: ') # This is to get the email from users
user_email = user_email.strip() # Cleaning the code for easier reading 

print(user_email) # This will display the user's email

print(len(user_email)) # While this will show the index count

# Second the validation process, these are where we need to find the points to validate an Email
point_1 = (user_email[-4] == '.') # Finding the '.' in user's email
point_2 = ('@' in user_email[-5 :: -1]) # Finding the '@' in user's email
point_3 = (user_email[0] != '@') # Checking for any characters before the '@' 
point_4 = (' ' not in user_email)# Checking for no spaces in the email address

# Third we combine all the points into one vaild string
Vaild = point_1 and point_2 and point_3 and point_4 

# Fourth we display a message for the Users
if Vaild is True:
    print('Your email is vailed, enjoy your subscription.') # This will display if the email was type correctly  

if Vaild is False:
    print('Sorry your email is not valid, please try typing in your email again.') # This will display if the email was type incorectly


'''
I know that the If and is true / false was not covered, But I just did it for the sake of the code.

Not too much of a fan of just raw data out in the terminal if I could clean it up for the users
'''