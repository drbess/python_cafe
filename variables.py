""" My bank account example """

'''
# Store "1000" in a variable called "BALANCE"
BALANCE = 1000

""" We define a function "withdraw" that contains two parameters """
def withdraw(current_balance, amount):
    current_balance -= amount
    print('Withdrawing money ...')
    return current_balance


def deposit(current_balance, amount):
    current_balance += amount
    print('Depositing money.')
    return current_balance


balance = withdraw(balance, 100)
balance = withdraw(balance, 50)
balance = balance + 10
balance = deposit(balance, 100)

print(balance)
'''
'''
#################################################################
'''
""" Here we define three variables """
fname = 350
mname = 550
lname = 650

print(fname, mname, lname, sep=",/#* ")

TotalApples = int(fname + mname * lname)

print("The total number of apples is: ", TotalApples)
