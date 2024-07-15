

user_input = input('please type "ready" to login or type "create login": ')

lst1 = []
lst2 = []

user = 'asap'
word = 'rocky'


for lo in user_input:
    if user_input == 'create login':
        lst1 = [(item) for item in input("Enter new username : ").split()]
        lst2 = [item for item in input("Enter new password : ").split()]
        print(f'New user created, {lst1} is your username. And {lst2} is your password')
    break

for po in user_input:
    if user_input == 'ready':
        next = input('please enter username: ')
        text = input('enter pass: ')
        if next == user and text == word:
            print('logged in')
        
        else: print('Error incorrect username or password. Please try again')
        break



