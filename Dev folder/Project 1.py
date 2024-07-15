


lst1 = []
lst2 = []

user_input = print('please type "ready" to login or type "create login": ')
ready = input('ready')
create = input('create login')
while True:
    if user_input == 'create login':
        point1 =input('Enter new username')
        lst1.append((point1))
        point2 = input('Enter password: ')
        lst2.append(input(point2))
        print(f'New user created, {lst1} is your username. And {lst2} is your password')


    if user_input == 'ready':
        next = input('please enter username: ')
        text = input('enter pass: ')
        if next == lst1 and text == lst2:
            print('logged in')
        
    else: print('Error incorrect username or password. Please try again')
       



