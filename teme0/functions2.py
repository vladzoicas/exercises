def get_name():
    name = input('What is your name? ')
    return name

def say_name(name):
    print('Your name is {}.'.format(name))

def get_and_say_name():
    """get and display name"""
    name = get_name()
    say_name(name)

get_and_say_name()
