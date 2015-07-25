'''
Created on Jul 24, 2015

@author: Tim 
'''

import random

if __name__ == '__main__':
    pass

'''Given: two lists of random int. Need to create third list containing only unique elements'''

first_list = []
second_list = []
d = {}
result = []
how_many_integers = 10
max_int = 100

for i in range (0, how_many_integers):
    first_list.append(random.randrange(max_int))
    second_list.append(random.randrange(max_int))

print('First list:', first_list)
print('Second list:', second_list)

for i in range (0, how_many_integers):
    if first_list[i] in d.keys():
        d[first_list[i]] += 1
    else:
        d[first_list[i]] = 1
        
    if second_list[i] in d.keys():
        d[second_list[i]] += 1
    else:
        d[second_list[i]] = 1
    
print('Dictionary: ', d)

for i in range(len(first_list)):
    if first_list[i] in d.keys():
        if d[first_list[i]] < 2:
            result.append(first_list[i])

for i in range(len(second_list)):
    if second_list[i] in d.keys():
        if d[second_list[i]] < 2:
            result.append(second_list[i])
    
print('Result: ', result)
    
    
    
    