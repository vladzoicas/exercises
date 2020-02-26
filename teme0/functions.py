def say_hi():
    print('Hi')

say_hi()

def say_name(name):
    print('Hi {}!'.format(name))

say_name('Jason')
say_name('Vlad')

def say_something(something = 'there'):
    print('Say {}!'.format(something))

say_something()
say_something('Something else!')

def say_double(first = 'Miha', last = 'Malina'):
    print('Ce faci {} {}?'.format(first, last))

say_double()
say_double('Cosmin', 'Mihai')

def say_hi2(first, last='Doe'):
    """Say hello."""
    print('Hi {} {}!'.format(first, last))

help(say_hi2)

def is_odd(number):
    """Determine if a number if odd."""

    if number % 2 == 0:
        return False
    else:
        return True

print(is_odd(7))
