class Person:
    def __init__(self, first_name, last_name, age=25):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def say_hello(self):
        return f"Hello, {self.first_name} {self.last_name}"


ivan = Person('Ivan', 'Ivanov')
georgi = Person('Georgi', 'Georgiev')

print(ivan.say_hello())
print(georgi.say_hello())


