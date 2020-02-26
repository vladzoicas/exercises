while True:
    n = (input('Please enter the number: '))
    try: 
        n = int(n)
    except ValueError:
        print('Please enter a valid number! ') 
    else: break

def isPrime(n):
    if n < 1:
        return False
    if n in [1, 2 ,3 ,5]:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 2
    while i < n ** 0.5:
        if n % i == 0:
            return False
        i = i + 1  
    
    return True

def divizoriPrimi(n):
    i = 2
    if isPrime(n) == True:
        return n
    while i <= n // 2:
        if n % i == 0:
            if isPrime(i) is True:
                print(i)
        i = i + 1
    return print('Acestia au fost divizorii primi ai numarului ', n)

print(isPrime(n))
print(divizoriPrimi(n))








