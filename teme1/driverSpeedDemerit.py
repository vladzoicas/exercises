driverSpeed = ''

while True:
    driverSpeed = (input('Please enter the first number: '))
    try: 
        driverSpeed = int(driverSpeed)
    except ValueError:
        print('Please enter a valid number, please') 
    else: break

def demeritPoints(speed):
    points = 0
    if speed <= 70:
        return 'Ok'
    elif speed <= 74:
        return 'A bit too fast'
    elif speed > 130:
        return 'License suspended'
    else: points = (speed - 70) // 5,
    return points

print(demeritPoints(driverSpeed))