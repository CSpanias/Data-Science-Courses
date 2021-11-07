# 5.1 
animals = ['mouse', 'horse', 'duck']
animal = 'dog'
print(f'Is animal == dog? I predict True!')
print(animal == 'dog')

print(f'\nIs animal == mouse? I predict False!')
print(animal == 'mouse')

# 5.2 
print(f'\nIs animal not a dog? I predict False!')
print(animal != 'dog')

print(f'\nIs mouse bigger than dog? I predict True!')
print('mouse' > animal)

print(f'\nIs wolf bigger than dog? I predict True!')
print('wolf' > animal)

print(f'\nIs wolf or turtle bigger than dog? I predict True!')
print(('wolf' > animal) or ('turtle' > animal))

print(f'\nIs wolf and turtle bigger than dog? I predict True!')
print(('wolf' > animal) and ('turtle' > animal))

print(f'\nIs wolf or turtle bigger than dog? I predict True!')
print(('wolf' > animal) | ('turtle' > animal))

print(f'\nIs wolf and turtle bigger than dog? I predict True!')
print(('wolf' > animal) & ('turtle' > animal))

print(f'\nIs wolf or turtle bigger than dog? I predict True!')
print(('wolf' > animal) or ('turtle' > animal))

print(f'\nIs horse in the list? I predict True!')
print('horse' in animals)

print(f'\nIs cat not in the list? I predict True')
print('cat' is not animals)