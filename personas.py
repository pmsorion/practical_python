

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello, my name is {} and I am {} years old'.format(self.name, self.age))


if __name__ == '__main__':
    person = Person('Frank', '35')

    print('The user {} have {} years old'.format(person.name, person.age))
    person.say_hello()
