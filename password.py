from os import urandom
from random import choice, shuffle
import pdb
import string
from sys import argv

char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
             'nums': '0123456789',
             'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
            }

def pick_char():
    return choice(string.punctuation + string.ascii_letters + string.digits) 

def upper_cased_list(array):
    return [char.upper() for char in array]

def set_password_length():
    if len(argv) > 1:
        return int(argv[1])
    else:
        return 30
        

def duplicate_found(password):
    pass_length=len(password)

    if pass_length==0:
        return False
    elif password[-1].upper() in  upper_cased_list(password[:-1]):
        return True
    return False

def generate_pass(length=set_password_length()):
    password = []

    while len(password) < length:
        key = choice(char_set.keys())
        a_char = pick_char() 

        if a_char in char_set[key]:
            if not duplicate_found(password):
                password.append(a_char)
            else:
                password.pop()

    return ''.join(password)


if __name__ == '__main__':
    print generate_pass()
