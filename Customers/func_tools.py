import random
import string


def generateTransID(key_length=25):
    key = ''
    chars = string.printable[:62]
    for i in range(key_length):
        key += random.choice(chars)
    return key
