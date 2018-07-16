

class Person:

    def __int__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return '{} {} is {} years old'.format(self.first_name, self.last_name, self.age)


person = Person('John', 'Smith', 32)

print(person)
