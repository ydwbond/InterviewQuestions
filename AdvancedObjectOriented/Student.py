from AdvancedObjectOriented.Personnel import Personnel


class Student(Personnel):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.class_list = [ ]

    def __repr__(self):
        return f"<Student Name {self.name}, student_id {self.student_id}, class list {[ c for c in self.class_list ]}>"

    @property
    def highest_score(self):
        t = 0
        for s in self.class_list:
            if t<= s["score"]:
                t = s["score"]
        return t

    @highest_score.setter
    def highest_score(self,value):
        t = 0
        highest_score_location = 0
        i = 0
        for s in self.class_list:
            if t <= s["score"]:
                t = s["score"]
                highest_score_location = i
            i += 1
        self.class_list[highest_score_location]["score"] = value

