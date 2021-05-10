x = int(input())
y = int(input())
x = x / y
y = y / x
print(y)

x = 1
y = 2
z = x
x = y
y = z
print(x, y)

z = y = x = 1
print(x, y, z, sep='*')

y = 2 + 3 * 5
print(y)

print(1 / 1)

t = input()
r = int(input())
print(t * r)