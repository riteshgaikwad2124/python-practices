class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def stud(self):
        print("I am a student")


stud1 = Student("abc", 18, 66)
stud1.display()
stud1.stud()

stud1.marks = 97
stud1.name = "xyz"

stud1.display()
print("Marks:", stud1.marks)