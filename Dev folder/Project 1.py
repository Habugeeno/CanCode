
lst1 = ['asap']
lst2 = ['rocky']
tommy = ['1','2', '3', '4', '5' ,'6', '7', '8','9','0']


while True:
    user_input = input('please enter Username or type "+": ')

    if user_input == '+':
        user = lst1.append(input('Enter new username: '))
        word = lst2.append(input('Enter new password: '))
        if user in tommy:
            print(f'New user created, {lst1} is your username. And {lst2} is your password')
        else:
            print('nope')
            
    if user_input in lst1:
        pch = input('Please enter your password: ')
        if pch in lst2:
            print('Logged on')
            break
        
            

    if user_input != lst1 or lst2 or ' ':
        print('no')  

        
    
    



