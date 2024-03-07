# TODO: Add all datatypes here

# Floating

# for integers
print(float(10))

# for floats
print(float(11.22))

# for string floats
print(float("-13.33"))

# for string floats with whitespaces
print(float("     -24.45\n"))

# string float error
print(float("abc"))


"""
########## Complex Numbers ##########

a = 2+3j
print('a =',a)
print('Type of a is',type(a))

b = -2j
print('b =',b)
print('Type of b is',type(a))

c = 0j
print('c =',c)
print('Type of c is',type(c))

"""

"""
########## Boolean ########## 

test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))
"""

"""
########## String ##########

# bytes
b = bytes('pythön', encoding='utf-8')

print(str(b, encoding='ascii', errors='ignore'))

Here, the character 'ö' cannot be decoded by ASCII. Hence, it should give an error. 
However, we have set the errors ='ignore'. 
Hence, Python ignores the character which cannot be decoded by str()

"""

"""
########## List ##########
# Using the class method again


# objects of this class are iterators
class PowTwo:
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
        
    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        result = 2 ** self.num
        self.num += 1
        return result

pow_two = PowTwo(5)
pow_two_iter = iter(pow_two)

print(list(pow_two_iter))

"""

"""
########## Tuples ##########

t1 = tuple()
print('t1 =', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2 =', t2)

# creating a tuple from a string
t1 = tuple('Python')
print('t1 =',t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)
"""

"""
########## Dict ##########

numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)
"""

"""
########## Set ##########

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

# print_num is an iterable
print_num = PrintNumber(5)

# creating a set
print(set(print_num))
"""

# Complex datatypes, the syntax of complex() would be complex([real[, imag]]). Example below


z = complex(2, -3)
print(z)

z = complex(1)
print(z)

z = complex()
print(z)

z = complex('5-9j')
print(z)


# A Frozenset. The syntax for frozenset([iterable]) Example below

# This is a random dictionary
person = {"name": "Legend", "age": 25, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)


# Bytes. the syntax for bytes([source[, encoding[, errors]]]). Example below

size = 5

arr = bytes(size)
print(arr)


# bytearray syntax bytearray([source[, encoding[, errors]]]). Example Below:


string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)


# Memory view syntax memory view(obj). Example below

# Modify internal data
# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)

mv = memoryview(random_byte_array)

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', random_byte_array)
