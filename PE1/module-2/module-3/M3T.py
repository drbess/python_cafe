# Answers to the Module 3 Test

#1
# An operator able to check whether two variables
# are equal is coded as "=="

"""
#2 How many hashes will the following snippet
send to the console (Solution - 4)
"""
var = 1
while var < 10:
    print("#")
    var = var << 1

# 3 
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

# 4
nums = [1, 2, 3]
vals = nums
del vals[1:2]

#5
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

# 6 How many elements does my_list contain?
my_list_3 = [i for i in range(-1, 2)]
print(my_list_3)

#7
my_list_4 = [1, 2, 3]
for v in range(len(my_list)):
    my_list_4.insert(1, my_list_4[v])
print(my_list_4)

#8
my_list_5 = [3, 1, -2]
print(my_list_5[my_list_5[-1]])

#9
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

#10
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")

#11
my_list_6 = [[0, 1, 2, 3] for i in range(2)]
print(my_list_6[2][0])

#12
for i in range(1):
    print("#")
else:
    print("#")

#13
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

#14
vals = [0,1,2]
vals.insert(0, 1)
del vals[1]

#15
t =[[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]

print(s)

#16
nums_1 = [1,2,3]
vals = nums_1[-1:-2]

#17
i = 0
while i <= 3:
    i += 2
    print("*")

#18
a = 1 
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

#19
z = 10
y = 0
x = y < z and z > y or y > z and z > y

#20
x = 1 
x = x == x
