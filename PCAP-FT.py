# PCAP - Final Test

#Q1
from typing_extensions import Self


def fun(x):
    return 1 if x % 2 != 0 else 2

print(fun(fun(1)))


#Q2 - what is the "sys.stdout" stream associated with?

#Q3 - output
my_string_1 = 'Bond'
my_string_2 = 'James Bond'

print(my_string_1.isalpha(), my_string_2.isalpha())

#Q4 - a package directory/folder may contain a file intended
# __init__.py

#Q5
def fun(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s


for x in fun(3):
    print(x, end='')


#Q6 - output
class Class:
    def __init__(self):
        pass

#Q7 - directory/folder created by Python used to store pyc files
# __pycache__

#Q8 - output
class A:
    A = 1
    def __init__(self, v=2):
        self.v = v + A.A
        A.A += 1

    def set(self, v):
        self.v += v
        A.A += 1 
        return

a = A()
a.set(2)
print(a.v)

#Q9 what is the expected output module.py
print(__name__)

# Skipped 10

#Q11
class A:
    def __init__(self):
        pass
    
    def f(self):
        return 1
    
    def g():
        return Self.f()

a = A()
print(a.g())

# Skipped question 12

#Q13 functions provided by the os module
#mkdr()

#Q14
t = (1, )
t = t[0] + t[0]
print(t)

#Q15
my_list = [1,2,3,4]

my_list = list(map(lambda x: 2*x, my_list))
print(my_list)

#Q16
d = {1: 0, 2: 1, 3: 2, 0: 1}
x = 0

for y in range(len(d)):
    x = d[x]

print(x)

#Q17
v = 1 + 1 // 2 + 1 / 2 + 2
print(v)

#Q18 - output
class A:
    def __init__(self, name):
        self.name = name

a = A("class")
print(a)

#Q19
x = """
"""
print(len(x))

#Q20
 
def fun(par2, par1):
    return par2 + par1

print(fun(par2=1, 2))

#Q21 - output
x = "\"
print(len(x))

#Q22 - a finally: branch inside the try: block

#Q23
my_list_2 = [[c for c in range(r)] for r in range(3)]

for element in my_list_2:
    if len(element) < 2:
        print()

#Q24
class A: 
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(A, B):
    def c(self):
        self.a()

o = C()
o.c()

#Q25 - output
from datetime import timedelta

delta = timedelta(weeks=1, days=7, hours=11)
print(delta)

#Q26 - output
def fun(d,k,v):
    d[k] = v 

my_dictionary = {}
print(fun(my_dictionary, '1', 'v'))

#Q27 - output
i = 4

while i > 0:
    i -= 2
    print('*')
    if i == 2:
        break
    else:
        print("*")

#Q28 - output
x, y, z = 3, 2, 1
z, y, x = x, y, z
print(x, y, z)

#Q29 - import function is invalid

#Q30
x = 16
while x > 0:
    print('*', end='')
    x //= 2


#Q31 - output
my_string_3 = 'abcdef'

def fun(s):
    del s[2]
    return s

print(fun(my_string_3))

#Q32 - output
class A:
    def __init__(self, v):
        self._a = v + 1

a = A(0)
print(a._a)

#Q33 - output
print(len([i for i in range(0, -2)]))

#Q34
d = {'one': 1, 'three': 3, 'two': 2}
for k in sorted(d.values()):
    print(k, end=' ')

#Q35 - output
import os
os.makedirs('picture/thumbnails')
os.rmdir('picture')

# Skipped 36

#Q37 - output
def fun(a, b, c=0):
    # function body

#Q38 - output
from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%Y/%m/%d %H:%M:%S'))

#Q39 - Exception
# The Exception class contains a property named
# args what is it?

#40 - output
print(len((1, )))

##### NOT NUMBERED #####
class X:
    pass

class Y(X):
    pass

x = X()
z = Z()
print(isinstance(x, Z), isinstance(z, X))

s = 'ARE YOU WITH ME, OR NOT!!!!'
q = s.readlines()
print(q)

z = 2
y = 1
x = y < z or z > y and y > z or z < y

a = True
b = False
a = a or b
b = a and b 
a = a or b
print(a, b)

print("a", "b", "c", sep="'")

# The below code is erroneous
try:
    raise Exception
except:
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b")

x = "\"
print(len(x))

class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'A'))

my_list_4 = [1, 2, 3, 4]

my_list_4 = list(map(lambda x: 2*x, my_list_4))
print(my_list_4)

x, y, z = 3, 2, 1
z, y, x = x, y, z
print(x, y, z)

import calendar

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

d = {1: 0, 2: 1, 3: 2, 0: 1}
x = 0

for y in range(len(d)):
    x = d[x]

print(x)

class A:
    A = 1
    def __init__(self):



d = {'one': 1, 'three': 3, 'two': 2}

for k in sorted(d.values()):
    print(k, end=' ')


t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
print(t)

# try-except-finally
try:
    raise Exception
except BaseException:
    print("a", end='')
else:
    print("b", end='')
finally:
    print("c")

str_1 = 'string'
str_2 = str_1[:]

# values 1 and 2
y = input()
x = input()
print(x + y)


class A:
    pass

class B: 
    pass

class C(A, B):
    pass

print(issubclass(C,A) and issubclass(C, B))

d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]

for x in d.keys():
    print(d[x][1], end="")


def a(x):
    def b():
        return x + x
    return b

x = a('x')
y = a('')
print(x() + y())




