animals = ['bird', 'bear', 'bear', 'pig', 'cow', 'horse', 'dog', 'bear', 'wolf']

print(animals)

for animal in animals:
    print(animal.upper())

index = 0
count = 0

while index < len(animals):
    if animals[index] == 'bear':
        animals.pop(index);
        count += 1
    index += 1

print(count)
print(animals)

for number in range(3):
    print(animals[number])

print(animals)

for number in range(1, 3):
    print(animals[number])
