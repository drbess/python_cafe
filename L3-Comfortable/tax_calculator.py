# TODO: Clean up code, test and add description

# A tax calculator

income = float(input("Enter the annual income: "))

tax = round(income, 0)


if income < float(85528):
    print("The tax is:", tax, "thalers")

elif income > float(85528):
    print("The tax is:", tax, "thalers")