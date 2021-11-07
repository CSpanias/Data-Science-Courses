# 5.8, 5.9
names = ['admin', 'user_1', 'user_2', 'user_3', 'user_4']

if names:
    for name in names:
        if name == 'admin':
            print(f'Hello {name}. Would you like to see a status report?')
        else: # name != 'admin'
            print(f'Hello {name}. Thank you for logging in again.')
else:
    print('We need to find some users!')

# 5.10
current_users = ['admin', 'user_1', 'user_2', 'user_3', 'user_4']
new_users = ['User_1', 'USER_4', 'user_5', 'user_6', 'user_7']

for new_user in new_users:
    new_user = new_user.lower()
    if new_user in current_users:
        print(f'The username {new_user} is not available. Enter a new username.')
    else: # if new_user not in current_users
        print(f'The username {new_user} is available for use.')

# 5.11
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else: # number != 1 | number != 2 | number != 3
        print(f'{number}th')

