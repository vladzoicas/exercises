animals = ['bird', 'wolf', 'bear', 'pig', 'cow', 'horse', 'dog']

some_animals = animals[1:4]
print('some animals: {}'.format(some_animals))

first_two = animals[0:2]
print('First two animals: {}'.format(first_two))

print(animals)

last_two = animals[-2:]
print('Last two animals: {}'.format(last_two))

try: cat_index = animals.index('cat')
except: cat_index = 'no cats found.'
print(cat_index)
