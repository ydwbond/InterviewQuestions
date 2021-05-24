from AdvancedObjectOriented.Student import Student
from AdvancedObjectOriented.Teacher import Teacher
from AdvancedObjectOriented.Database import Database


st1 = Student("Tim",1)

st1.class_list.append({"subject":"English", "score":100})
st1.class_list.append({"subject":"Math", "score":23})
st1.class_list.append({"subject":"Science", "score":98})

print(st1.highest_score)

st1.highest_score = 21
print(st1.highest_score)
st1.save()
st2 = Student("John",2)
st2.save()

t1 = Teacher("Mr Planto", 1, 120000)
t1.save()


Database.display()
