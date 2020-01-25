class Employee:
    pass


class EmployeeManager:
    def __init__(self):
        self.person = []

    def add_emp(self, emp):
        self.person.append(emp)

    def __iter__(self):
        return EmployeeIterator(self.person)


class EmployeeIterator:
    def __init__(self, target):
        self.target = target
        self.index = 0

    def __next__(self):
        if self.index == len(self.target):
            raise StopIteration
        temp = self.target[self.index]
        self.index += 1
        return temp

m01 = EmployeeManager()
m01.add_emp(Employee())
m01.add_emp(Employee())
m01.add_emp(Employee())

iterator = m01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break