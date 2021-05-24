from AdvancedObjectOriented.Personnel import Personnel

class Teacher(Personnel):
    def __init__(self,name, teacher_id, salary):
        super().__init__(name)
        self.teacher_id = teacher_id
        self.salary = salary

    def __repr__(self):
        return f"<Teacher {self.name} with teacher _id {self.teacher_id} and Salary of {self.salary}>"

