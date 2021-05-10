"""
x = float(input("Enter value for x: "))

y = (1 / x + 1 / x + 1 / (x + 1/x))

print("y =", y)

=========================================
1 y = 0.6000000000000001

10 y = 0.09901951266867294

100 y = 0.009999000199950014

-5 y = -0.19258202567760344
"""


hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print("\nThe start time in hours is: " + str(hour % mins % dura))

print("\nThe start time in minutes is: " % str(mins))

print("\nThe event duration is:" % str(dura))
