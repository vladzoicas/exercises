while True:
    textinput1 = (input('Please enter the first number: '))
    try: 
        textinput1 = int(textinput1)
    except ValueError:
        print('Please enter a valid number, please') 
    else: break

while True:
    textinput2 = (input('Please enter the second number: '))
    try: 
        textinput2 = int(textinput2)
    except ValueError:
        print('Please enter a valid number, please') 
    else: break

def max_of_two_numers(first, second):
    max = 0
#    first = textinput1
#    second = textinput2
    if first > second:
        max = first
    elif first == second:
        max = first
    else: max = second

    return max;

print(max_of_two_numers(textinput1, textinput2))