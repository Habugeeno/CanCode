
lst1 = []
lst2 = []

while True:
    user_input = input('please enter Username or type "create login": ')

    if user_input == 'create login':
        user = lst1.append(input('Enter new username: '))
        word = lst2.append(input('Enter new password: '))
        print(f'New user created, {lst1} is your username. And {lst2} is your password')
        
            
    if user_input == user:
        print('joo')
    
    if user_input == 'log off':
        print('goodbye')
        break       




