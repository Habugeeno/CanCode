
lst1 = ['asap']
lst2 = ['rocky']
user = lst1
word = lst2

req1 = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
req2 = ('!', '?', '@', '#', '$', '^', '&', '*', '_', '-')
req = req1 + req2

msgs = ('Logged on, Welcome to VSS', 'Error, invalid username or password. Please try again',
         'Error, New username or password is missing paramitors. Removing user and password ')

logged = msgs[0]
loge = msgs[1]
loge1 = msgs[2]
 


while True:
    user_input = input('please enter Username or type "+": ')
    
    if user_input == '+':
        user = input('Enter new username: ')
        if user == user.lower():
             user not in lst1
             lst1.append(user)
             word = input('Enter new password: ')
             if word not in lst2:
                lst2.append(word)
                print(f'username:{lst1}. password: {lst2}')
                for lo in word:
                    if lo in req1:
                        print('yay')
                    elif lo not in req1:
                        print(f'{loge1}{lst1}{lst2}')
        else:
            print('piss')        
            
            
    if user_input in lst1:
        pch = input('Please enter your password: ')
        if pch in lst2:
            print(logged)
            break
    if user_input == lst1 or lst2 == False:
        print(loge)  

        
    


'1,2,3,4,5,6,7,8,9,0'

('1'), ('2'), ('3'),('4'),('5'),('6'),('7'),('8'),('9'),('0')

(1), (2), (3), (4), (5), (6), (7), (8), (9), (0)

''' !, ?, @, #, $, ^, &, *, _, - '''

('!'), ('?'), ('@'), ('#'), ('$'), ('^'), ('&'), ('*'), ('_'), ('-')

'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'

'!', '?', '@', '#', '$', '^', '&', '*', '_', '-'

# for check in word:
#                     if check in req1 and req2:
#                         print('yes')
#                     else:
#                         print('no')