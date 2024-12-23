# 1
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        a = input("Enter email: ")
        if a == self.email:
            self.__password = new_password
            return "Password changed"
        else:
            return "Email is incorrect"
    def check_password(self, password):
        if password == self.__password:
            return True
        else:
            return False
obj = UserAccount("Alex", "123@ht.com", "0000")
print(obj.set_password("1111"))
print(obj.check_password("0000"))

# 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return self.make, self.model
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        return self.make, self.model, self.fuel_type
obj = Car("Toyota", "Prado", "Diesel")
print(obj.get_info())

















