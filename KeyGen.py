import string, itertools

charSet = string.printable[:36] # [0-9a-z]
for key in itertools.product(charSet, repeat = 5): # ghostbin ids are length 5
    print key

'''
# grep  "'n', 'z', 'n', '8', 't'" keys.txt
#for subset in itertools.combinations(stuff, 5):
#for subset in itertools.permutations(stuff, 5):
#    print(subset) 
'''     
