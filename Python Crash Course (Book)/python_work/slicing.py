# 4.10
animals = ['dog', 'cat', 'fox', 'horse', 'mouse']

print('The first three animals in the list are:',animals[:3], '\n')




# 4.11
animals_2 = animals[:]
animals_2.append('donkey')

print('My favorite animals are:')
for animal in animals:
    print(animal)

print('My favorite animals_2 are:')
for animal in animals_2:
    print(animal)

# 4.12
my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
my_friends_foods = my_foods[:]
my_friends_foods.append('souvlaki')

for food in my_foods:
    print(food)

for food in my_friends_foods:
    print(food)