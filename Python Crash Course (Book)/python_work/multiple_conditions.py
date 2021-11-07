# 5.3
alien_color = 'red'

if alien_color == 'green':
    print('You have just earned 5 points!')

if alien_color == 'red':
    print('You have just earned 5 points!')

# 5.4

if alien_color == 'green':
    print('You have just earned 5 points!')
else: # alien_color != 'green':
    print('You have just earned 10 points!')

if alien_color == 'red':
    print('You have just earned 5 points!')
else: # alien_color != 'red':
    print('You have just earned 10 points!')

# 5.5
if alien_color == 'green':
    print('You have just earned 5 points!')
elif alien_color == 'yellow':
    print('You have just earned 10 points!')
else: # alien_color != 'green' and alien_color != 'yellow':
    print('You have just earned 15 points!')

alien_color = 'yellow'
if alien_color == 'green':
    print('You have just earned 5 points!')
elif alien_color == 'yellow':
    print('You have just earned 10 points!')
else: # alien_color != 'green' and alien_color != 'yellow':
    print('You have just earned 15 points!')

alien_color = 'green'
if alien_color == 'green':
    print('You have just earned 5 points!')
elif alien_color == 'yellow':
    print('You have just earned 10 points!')
else: # alien_color != 'green' and alien_color != 'yellow'
    print('You have just earned 15 points!')


# 5.6 
age = 30

if age < 2:
    print('The person is a baby.')
elif age < 4:
    print('The person is a toddler.')
elif age < 13:
    print('The person is a kid.')
elif age < 20:
    print('The person is a teenager.')
elif age < 65:
    print('The person is an adult.')
else: # age >= 65
    print('The person is elder.')

# 5.7 
favorite_fruits = ['banana', 'apple', 'melon']

if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'melon' in favorite_fruits:
    print('You really like melons!')