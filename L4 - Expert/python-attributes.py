class Vehicle:

    # engine = "Hemi"
    cylinders = 8

    def __init__(self, pickup):
        self.pickup = pickup


c1 = Vehicle("Ram Rebel")
print(c1.pickup)
print(f"The Ram Rebel is a pickup truck with {c1.cylinders} cylinders")
