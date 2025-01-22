class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
         print(f"Person(name='{self.name}', age={self.age})")
def print_person2(p:Person):
    print ( f'{p.name} and {p.age} ')

p = Person("Alice", 30)
print("hi")
print(p.print_person())  # Output: Person(name='Alice', age=30)
print("hi")
print_person2(p)
