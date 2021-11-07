# 6.4
glossary = {
    'f-string': 'means format string',
    'dictionary': 'stores key-value pairs',
    'tuple': 'is an immutable list',
    'python': 'originates from monty-python!',
    'import_this': 'prints the zen of python',
    'set()': 'print only unique values',
    '.items()': 'loops through the key-value pairs',
    '.values()': 'loops through the values only',
    '.keys()': 'loops through the keys only',
}

for key, value in glossary.items():
    print(f'\n{key} {value}.')

# 6.5
rivers = {
    'nile': 'egypt',
    'pineios': 'greece',
    'erdre': 'france'
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.\n')

for river in rivers: # or for river in rivers.keys():
    print(f'{river.title()}\n')

for country in rivers.values():
    print(f'{country.title()}\n')

# 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['erin', 'mike', 'jen', 'phil']

for name in favorite_languages:
    if name not in friends:
        print(f'{name.title()} you should take the poll!')
    else: # name in friends
        print(f'{name.title()}, thank you for taking the poll!')