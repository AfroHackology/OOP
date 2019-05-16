class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    names = input([])
    tardies = bool(False)

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.apply_raise())

    def


emp_1 = Employee('Greg', 'X', 50000)
emp_2 = Employee('Test', 'X', 60000)

# Get information of instance, class or attribute by using __dict__
# print(emp_1.__dict__)

# Changed Employee raise amount
# Employee.raise_amount = 1.05
# Specify the instance you want to apply a raise to
# emp_1.raise_amount = 1.05

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_1.raise_amount)


"""" Both of these work the same but one needs an instance to be called inside
 the parens and the other
 
print(emp_1.fullname()) # This is an instance and doesn't need self to be called because it is done automaticly
print(Employee.fullname(emp_1)) # Called on class so it doesn't know what instance to print so give it one
print(emp_1.fullname()) 

"""
# # Called emp1.pay and then applied the raise therefore it applied the raise
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)