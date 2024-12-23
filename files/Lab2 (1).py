# 1
a = input()
def greet(a):
    print("Hello, ", a)
greet(a)

# 2
def square(number):
    print(number**2)
square(2)

# 3
def max_of_two(x, y):
    if x>y:
        print(x)
    elif x<y:
        print(y)
    else:
        print(x)
max_of_two(2, 3)

# 4
def describe_person(name, age=30):
    print("Name, ", name)
    print("Age, ", age)

describe_person("dfgd", 25)

# 5
def is_prime(number):
    if number>1 and all(number%i!=0 for i in range(2, int(number**2))):
        return True
    return False
