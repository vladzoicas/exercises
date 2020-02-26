while True:
    n = (input('Please enter the number: '))
    try: 
        n = int(n)
    except ValueError:
        print('Please enter a valid number! ') 
    else: break

i = 1

while i < n // 2:
    if n % i == 0: 
        print(i)
    i = i + 1


