'''
Assignment # 4: getting username and password
'''

# The key variables to login
sys_user_name,sys_user_pass = 'admin', 'password' 

# This is the client side input to log in
username = input('enter user name: ')
passcode = input('enter your passcode: ')

# The output of the login to determin a successfull login
if username == sys_user_name and passcode == sys_user_pass:
        print('logged on')
else:
    print('loggin failure')