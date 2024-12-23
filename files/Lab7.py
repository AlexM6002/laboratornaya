# 1
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        print(f"Имя: {self.name}")
        print(f"Id: {self.id}")
class Manager(Employee):
    def __init__(self, name = "ghfj", id = "khf", department="fhgjrhgjhf"):
        super().__init__(name, id)
        self.department = department
    def manage_project(self):
        print("Project created")
class Technician(Employee):
    def __init__(self, name = "", id = "", specialization = ""):
        self.name = name
        self.id = id
        self.specialization = specialization
    def perform_maintenance(self, choice):
        print(f"Выбрано {choice} выполнение")
class TechManager(Manager, Technician):
    employees = []
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id, department)
        super().__init__(name, id, specialization)
    def add_employee(self, employee):
        self.employees.append(employee)
    def get_info_team(self):
        for employee in self.employees:
            print(employee)
#1
obj1 = Employee("fhgjf", "128")
obj1.get_info()
#2
obj2 = Manager("fghfjhgj", "135", 'Sail')
obj2.manage_project()
#3
obj3 = Technician("fhgj", "Product", "fjhg")
obj3.perform_maintenance(1)
#4
obj4 = TechManager("fjhf", "fhgjf", "dhggfg", "fhjgfjhg")
obj4.add_employee(["1", "2"])
obj4.get_info_team()
