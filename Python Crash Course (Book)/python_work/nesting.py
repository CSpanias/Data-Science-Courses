# 6.7
person = {
    'first': 'maria',
    'last': 'savana',
    'age': 30,
    'city': 'athens',
}

person_1 = {
    'first': 'mitsos',
    'last': 'kolokis',
    'age': 40,
    'city': 'london',
}

person_2 = {
    'first': 'sam',
    'last': 'mcdougal',
    'age': 10,
    'city': 'edinburgh',
}

people = [person, person_1, person_2]

for person in people:
    print(f'\n{person}')

# 6.8
pet = {
    'kind': 'dog',
    'owners_name': 'sam',
}

pet_1 = {
    'kind': 'cat',
    'owners_name': 'euan',
}

pet_2 = {
    'kind': 'rabbit',
    'owners_name': 'doug',
}

pets = [pet, pet_1, pet_2]
for pet in pets:
    print(f'{pet}\n')

# 6.9
favorite_places = {
    'sam': ['venezuela', 'sydney', 'mikonos'],
    'harris': ['santorini', 'edinburgh', 'glasgow'],
    'euan': ['milan', 'london', 'moscow'],
}

for name, places in favorite_places.items():
    print(f'{name.title()} favorite places are:')
    for place in places:
        print(f'\t{place.title()}')

# 6.10
favorite_numbers = {
    'john': [3, 5, 6],
    'maria': [9, 7, 5],
    'harris': [10, 15],
    'sam': [15, 4, 5, 6],
    'euan': [32],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f'{name.title()} favorites numbers are:')
        for number in numbers:
            print(f'{number}.')
    else: # number < 1
        print(f'{name.title()} favorite number is: {number}.')

# 6.11
cities = {
    'athens': {
        'country': 'greece',
        'population': 11_000_000,
        'fact': 'overcrowded',
        },
    'edinburgh': {
        'country': 'scotland',
        'population': 400_000,
        'fact': 'green',
        },
    'london': {
        'country': 'england',
        'population': 4_000_000,
        'fact': 'overcrowded',
        }
    }

for city, city_info in cities.items():
    print(f'Information about {city.title()}:')
    for key, value in city_info.items():
        print(f'{key} : {value}')
    print('')

# 6.12
exercises = {
    'upper_body': ['bench press', 'row', 'flies', 'pullups', 'reverse flies', 'shoulder press'],
    'lower_body': ['squat', 'lunges', 'cossacks', 'leg curl', 'stiff-leg deadlift'],
    'core' : ['ab wheel', 'plank', 'situps', 'windmills', 'farmers carry'],
}

for body_part, exercises in exercises.items():
    print(f'The exercises for the {body_part} are the following:')
    for exercise in exercises:
        print(f'\t{exercise}')
