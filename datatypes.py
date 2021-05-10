'''Integer '''






'''
Complex datatype
The syntax of complex() would be complex([real[, imag]])

Example below
'''

z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)

'''
Frozenset
The syntax frozenset([iterable])

Example below
'''
# This is a random dictionary
person = {"name": "Legend", "age": 25, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)


'''
Bytes
THe syntax bytes([source[, encoding[, errors]]])

Example below
'''
size = 5

arr = bytes(size)
print(arr)

'''
bytearray syntax bytearray([source[, encoding[, errors]]])


Example Below
'''

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)


'''
Memoryview syntax memoryview(obj)

Example below
Modify internal data
'''
# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)

mv = memoryview(random_byte_array)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', random_byte_array)
