from NewEmployee import NewEmployee
import datetime

e1 = NewEmployee()
print(e1)
print(repr(e1))

e2 = eval(repr(e1))
print(e2)

e1.test()

# e1.basic = -100

e3 = NewEmployee("Mrugank", 7000000)
print(e3)
print(repr(e3))

# dt = date(year=2025,month=9,day=29)
# dt = datetime.date(2025,9,29)
# print(dt)
# print(repr(dt))

# dt2 = eval(repr(dt))
# print(repr(dt))
# print(dt2)

# e1.name = "Tom"
e1._name = "Jerry"
e1._basic = 100
print(e1)

print(NewEmployee.count_employees())

NewEmployee.set_count(150)

print(NewEmployee.count_employees())