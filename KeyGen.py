import string, itertools

charSet = string.printable[:36] # [0-9a-z]
for key in itertools.product(charSet, repeat = 5): # ghostbin ids are length 5
    print key
