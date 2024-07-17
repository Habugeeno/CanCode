
lst1 = ['asap']
lst2 = ['rocky']




while True:
    user_input = input('please enter Username or type "create login": ')

    if user_input == 'create login':
        user = lst1.append(input('Enter new username: '))
        word = lst2.append(input('Enter new password: '))
        print(f'New user created, {lst1} is your username. And {lst2} is your password')
    
        
            
    if user_input in lst1:
        pch = input('Please enter your password: ')
        if pch in lst2:
            print('Logged on')
            break
        
            

        if user_input != lst1 and lst2:
            print('no')  

        
    
    



