# 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(selfs):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")
# 2
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius
circle_10 = Circle(10)
print(circle_10.get_radius())
print(circle_10.set_radius(15))
    
