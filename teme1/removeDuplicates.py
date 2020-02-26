lista1 = ['pig','pig', 'cat', 'cat', 'hat', 'pig', 'dog', 'ding', 'cat', 1, 1 , 1, 'dong', 'ding']

def ifInList(a, lista3):
    j = 0
    while j < len(lista3) :
        if a == lista3[j]:
            return True
        j = j + 1
    return False
    

def noDuplicates():
    lista2 = []
    i = 0
    b = True
    c = ''
    while i < len(lista1):
        c = lista1[i]
        b = ifInList(lista1[i], lista2)
        if b == False:
            lista2.append(c)
        i += 1
    return print(lista2)
                    
print(noDuplicates())

my_set = {*lista1}
print(my_set)