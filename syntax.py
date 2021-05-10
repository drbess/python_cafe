# Lesson One Basic Syntax
passwordFile = open('passwdfile.txt')

secretPassword = passwordFile.read()

print('Enter your password.')

typedPassword = input()

if typedPassword == secretPassword:
    print('Access granted')


if typedPassword == '12345':
    print('Now why would you create a password like that man!!!.')


else:
    print('Access denied')

