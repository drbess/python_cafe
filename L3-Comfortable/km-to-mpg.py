# Conversion using kilometers to miles per gallon
# TODO: Add more conversion examples below
"""
1 kilometer equals 0.62137 miles.
Miles = kilometer * 0.62137
Kilometer = Miles / 0.62137

"""


def l100kmtompg(liters):
    miles = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784
    return miles / gallons


def mpgtol100km(miles):
    liters = 3.785411784
    kilometers = miles * 1000 / 1609.344
    km100 = kilometers / 100
    return liters / km100


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

"""
Expected Output
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757

"""