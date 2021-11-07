# scripts created on Sublime Text but executed on Jupyter Notebooks

# 7.1
car = input('What kind of car you would like to rent? ')
print(f'Let me see if I can find a {car}!')

# 7.2
people = input('Enter the number of people you would like a revervation for: ')
people = int(people)

if people > 8:
    print('You will have to wait for a table.')
else: # people <= 8
    print('Your table is ready.')

# 7.3
number = input('Enter a number: ')
number = int(number)

if number % 10 == 0:
    print(f'The number {number} is a multiple of 10.')
else: # number % 10 != 0
    print(f'The number {number} is not a multiple of 10.')