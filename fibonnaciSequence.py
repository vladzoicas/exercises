b = True
n = ''

def checkIfSmallerThan1(a):
    if a < 1:
        return True
    else: return False


while b == True:
    n = (input('Please enter a number bigger than 1: '))
    try: 
        n = int(n)
    except ValueError:
        print('Please enter a number bigger than 1:') 
    else: b = checkIfSmallerThan1(n)

def writeFibonnaci(c):
    lista = [1]
    count = 2
    suma = 0
    if c == 1: 
        return print(lista)
    lista.append(1)
    if c == 2:
        return print(lista)
    if c > 2:
        while count <= c - 1:
            suma = int(lista[count-1]) + int(lista[count-2])
            lista.append(suma)
            count = count + 1
    return lista      

print(writeFibonnaci(n))
