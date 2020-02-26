n = ''

n = (input('Please enter a string: '))

def inverseWords(a):
    str1 = ''
    str2 = ''
    i = 0
    c = False
    while i < len(a):
        if a[i] != ' ':
            str1 = str1 + a[i]
            i = i + 1
        else: 
            i = i + 1
            c = True
            str2 = ' '+ str2
        if c == True or i == len(a):
            str2 = str1  + str2 
            str1 = ''
            c = False
    
    return str2


print(inverseWords(n))


