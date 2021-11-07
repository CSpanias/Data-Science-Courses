# 4.3
for number in range(1,21):
	print(number)

# 4.4
#for number in range(1,1_000_001):
#	print(number)

# 4.5 
million_numbers = []
for number in range(1,1_000_001):
	million_numbers.append(number)

print(f'The maximum number is: {max(million_numbers)}\nThe minimum number is: {min(million_numbers)}\nThe sum is: {sum(million_numbers)}.')

# 4.6
for number in range(1,21, 2):
	print(number)

# 4.7
multiples_of_3 = []
for number in range(1,31):
	if 30%number == 0:
		multiples_of_3.append(number)

print(multiples_of_3)

# 4.8
for number in range(1,11):
	cube = number**3
	print(cube)

# 4.9
cube = [number**3 for number in range(1,11)]
print(cube)
