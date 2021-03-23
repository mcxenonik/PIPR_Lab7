class Person:
    def __init__(self, fname, lname, age=0):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def introduce(self):
        return f'My name is {self.first_name} My last name is {self.last_name}'
