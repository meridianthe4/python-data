from datetime import date
from Employees import Employee

e1 = Employee()
print(e1)

# dt = date(year=2025,month=9,day=29)
# print(dt)
# print(repr(dt))

print(repr(e1))

e2 = eval(repr(e1))
print(e2)
print(type(e2))

from Employees import NewEmployee

n1 = NewEmployee('PPP',45000)
n2 = NewEmployee('SSS', 80000)

NewEmployee.show_employee_count()

NewEmployee.set_count()
n3 = NewEmployee('Vedant' , 999999)
NewEmployee.show_employee_count()
print(n3)