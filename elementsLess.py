lista = []
n = 'a'

def printElementsUnder5(): #print less than 5

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    i = 0

    while i < len(a):
        if int(a[i]) >= 5:
            a.remove(a[i])
            i = i - 1
        i = i + 1    
    return a

print(printElementsUnder5())

def printOneLine():

    b = [1, 1, 5, 78, 3, 7, 56, 34, 3, 5 ,9 , 31, 12,]
    filtered = [item for item in b if item < 20]  #print in one line
    return filtered

print(printOneLine())


while n != '' :
    n = (input('Please enter a number: '))
    try: 
        n = int(n)
    except ValueError:
        print('Please enter a valid number! ') 
    lista.append(n)

lista.remove(lista[0])
lista.remove('')

while True:
    n = (input('Please enter the limit number: '))
    try: 
        n = int(n)
    except ValueError:
        print('Please enter a valid number! ') 
    else: break

i = 0
while i < len(lista):
    if int(lista[i]) >= n:
        lista.remove(lista[i])
        i = i - 1
    i = i + 1    
print(lista)