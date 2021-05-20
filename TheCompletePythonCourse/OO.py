class Student:
    def __init__(self, name, grades, gender):
        self.name = name
        self.grades = grades
        self.gender = gender
        #self.average = sum(grades)/len(grades)
    def average(self):
        return sum(self.grades)/len(self.grades)

    def __len__(self):
        return len(self.grades)

    def __getitem__(self, item):
        return self.grades[item]

    def __str__(self):
        return 'test'

    @staticmethod
    def te():
        print("test123")


st1 = Student(name="test",grades=[89,91,98,81,98],gender='Male')
print(st1.average())
print(st1.grades)

print(Student.average(st1))

print(len(st1))
print(st1.__getitem__(1))
print(st1.__len__())
print(st1[1])
print(st1)