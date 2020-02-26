import random
import string

def randomWeakPassword(stringLength):

    """Generate a random string of letters and digits """

    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

print ("The weak password is:  ", randomWeakPassword(5))

def randomStrongPassword(stringLength):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print ("The strong password is: ", randomStrongPassword(10) )