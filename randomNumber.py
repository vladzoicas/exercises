from random import randint

m = ''

while m != 'exit': #iesit din bucla cu exit
    
    def randomGenerateNumber(): # genereaza numar random
        a = randint(1,9)
        return a

    def checkIfInRange(a): # verifica daca numarul introdus e intre 1 si 9
        if a in range(1,10):
            return False
        else: return True


    def enterNumber(): # introduce numere de la tastatura 
        b = True
        while b == True:
            n = (input('Please enter a number between 1 and 9: '))
            try:
                n = int(n)
            except ValueError:
                print('Please enter a valid number between 1 and 9:') 
            else: b = checkIfInRange(n)
        return(n)

    def hasPlayerGuessed(): # introduce numere pana cand se nimereste 
        count = 0
        a = randomGenerateNumber()
 #   print(a)
        n = ''
        while a != n: 
            n = enterNumber() 
            count = count + 1
            if n > a: 
                print('too high')
            else: print('too low')
        return('You have guessed number:', a, 'It too you', count,' chances!')

    print(hasPlayerGuessed())
        
    m = (input('Write exit if you want to quit! '))        
    
