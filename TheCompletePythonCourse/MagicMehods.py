class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = []


    def update_grades(self,grade):
        self.grades.append(grade)


    @property
    def average_grade(self):
        return sum(self.grades)/len(self.grades)

    # used in debugger, if there is no __str__ in the class then print this
    def __repr__(self):
        return f'<Student name = {self.name}, age = {self.age}, grades = {self.grades}, this is from {self.__class__}>'


    def __len__(self):
        return len(self.grades)

    def __getitem__(self, item):
        return self.grades[item]

    #used in print
    # def __str__(self):
    #     return f'Student name = {self.name}, age = {self.age}, grades = {self.grades}'

    @classmethod
    def create_student(cls,name,age):
        return cls(name,age)

    @staticmethod
    def Add(a,b):
        return a + b

class WorkingStudent(Student):
    def __init__(self,name,age,salary=0):
        super().__init__(name,age)
        self.salary = salary
    def __repr__(self):
        return f'<this is from {self.__class__}>'

    def calculate_avg_salary(self):
        raise NotImplementedError('The application hasnt implemetned')

    def test_deprecation_warning(self):
        raise DeprecationWarning('still working but no good')
wst1 = WorkingStudent("Tom",20,18)
st = Student("Jack",18)

wst1.update_grades({"English":89})
wst1.update_grades({"Math":70})
wst1.update_grades({"Art":91})
print(wst1)

wst2 = WorkingStudent.create_student("Luke",20)
print(wst2)
st2 = Student.create_student("Jason",19)
print(st2)

print(WorkingStudent.Add(1,2))
print(Student.Add(2,3))
#wst1.calculate_avg_salary()
wst1.test_deprecation_warning()

wst1.update_grades({"English":89})
wst1.update_grades({"Math":70})
wst1.update_grades({"Art":91})
print(wst1)
print('final')
