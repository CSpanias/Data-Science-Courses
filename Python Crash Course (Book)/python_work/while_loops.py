# 7.4
prompt = '\nPlease enter your preferred pizza toppings:'
prompt += ('\nType "quit" when you are done.')

toppings = input(prompt)

while toppings != 'quit':
    print(f'{toppings} is added to the pizza!')
    toppings = input(prompt)

# 7.5
prompt = '\nPlease enter your age (in years)'
age = int(input(prompt))

if age < 3:
    price = 0
elif age <= 12:
    price = 10
else: # age > 12
    price = 15

print(f'The ticket price is {price}.')

# 7.6
# using conditional
# the program 7.4 uses conditioning

# using an active variable
prompt = '\nPlease enter your preferred pizza toppings:'
prompt += ('\nType "quit" when you are done.')

active = True

while active:
    toppings = input(prompt)
    
    if toppings == 'quit':
        active = False
    else: # toppings != 'quit'
        print(f'{toppings} is added to the pizza!')

# using break
prompt = '\nPlease enter your preferred pizza toppings:'
prompt += ('\nType "quit" when you are done.')

toppings = input(prompt)

while True:
    if toppings == 'quit':
        break
    else: # toppings != 'quit'
        print(f'{toppings} is added to the pizza!')
        toppings = input(prompt)

# 7.7
prompt = '\nPlease enter your preferred pizza toppings:'
prompt += ('\nType "quit" when you are done.')

toppings = input(prompt)

while True:
    if toppings == 'quit':
        break
    else: # toppings != 'quit'
        print(f'{toppings} is added to the pizza!')