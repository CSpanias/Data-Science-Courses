# 7.8
sandwich_order = ['prawn', 'double cheese', 'chicken', 'ham', 'egg']

finished_sandwiches = []

while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f'I made your {sandwich} sandwich!')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'Your {sandwich} sandwich is ready!')

# 7.9
sandwich_order = ['prawn', 'pastrami', 'double cheese', 'pastrami', 'chicken', 'ham', 'egg', 'pastrami']
finished_sandwiches = []
print('The deli has run out of pastrami!')

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    sandwich = sandwich_order.pop()
    print(f'I made your {sandwich} sandwich!')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'Your {sandwich} sandwich is ready!')

# 7.10
# create an empty dictionary
dream_vacation = {}

# set a flag indicating that the polling is active
polling_active = True


while polling_active:
    # set the prompt messages
    prompt_name = 'What is your name?\n '
    name = input(prompt_name)
    prompt_place = 'If you could visit one place in the world, where would you go? '
    place = input(prompt_place)

    # store the answer in the dictionary
    dream_vacation[name] = place

    # find out if anyone else wants to take the poll
    repeat = input('Is anyone else wants to take the poll? (yes/no) ')
    if repeat == 'no':
        polling_active = False

# polling is complete
print('---Poll Results---')
for name, place in dream_vacation.items():
    print(f'{name.title()} wants to visit {place.title()}.')




