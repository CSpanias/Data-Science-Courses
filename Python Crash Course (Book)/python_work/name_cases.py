# 2.3
name = 'maria kontostergiou'
print(f'{name.title()} is doing the Scarn!')

# 2.4
print(f'Her full name is: {name.upper()}')
print(f'Her full name is: {name.lower()}')
print(f'Her full name is: {name.title()}')

# 2.5
famous_name = 'jack london'
print(f'{famous_name.title()} once said: "I shall not waste my days in trying to prolong them. I shall use my time."')

# 2.6
message = f'{famous_name.title()} once said: "I shall not waste my days in trying to prolong them. I shall use my time."'
print(message)

# 2.7
name = ' Maria kontostergiou '
print(name)

name = name.rstrip()
name = name.lstrip()
name = name.strip()
print(name)

first_name = 'Maria'
last_name = 'kontostergiou'
full_name = f'{first_name}\n\t{last_name}'
print(full_name)