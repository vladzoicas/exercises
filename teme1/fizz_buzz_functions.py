fizzBuzzNumber = ''

while True:
    fizzBuzzNumber = (input('Please enter the first number: '))
    try: 
        fizzBuzzNumber = int(fizzBuzzNumber)
    except ValueError:
        print('Please enter a valid number, please') 
    else: break

#fizzBuzzNumber = (input('Please enter the first number: '))

def ifFizzBuzz(theNumber):
    if ((theNumber % 3 == 0) | (theNumber % 5 == 0)):
        return 'FizzBuzz'
    elif theNumber % 5 == 0:
        return 'Buzz'
    elif theNumber % 3 == 0:
        return 'Buzz'
    else: return 'Not Fizz Buzz'

print(ifFizzBuzz(fizzBuzzNumber))