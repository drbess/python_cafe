class Employee():
    pass
employee = Employee()
employee.salary = 140000
employee.firstname = 'Marcus'
employee.lastname = 'Garvey'


print(employee.firstname + "  "
      + employee.lastname + "  "
      + str(employee.salary) + "$")