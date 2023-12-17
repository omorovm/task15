from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    expirience = models.IntegerField()

    students = models.ManyToManyField(
        Student, 
        related_name='teachers'
    )

# >>> from ManytoManyApp.models import Student, Teacher
# >>> student1 = Student.objects.create(name='student1', age =15)
# >>> student2 = Student.objects.create(name='student2', age =16)
# >>> student3 = Student.objects.create(name='student3', age =17)
# >>> teacher1 = Teacher.objects.create(name='teacher1', subject='math', expirience=2)
# >>> teacher1.students.set([student1,student2])    #обращаемся к связи и добавляем студентов
# >>> teacher1.students
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f6529f2f5b0>
# >>> teacher1.students.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>
# >>> student1.teachers.all()
# <QuerySet [<Teacher: Teacher object (1)>]>
# >>> teacher2 = Teacher.objects.create(name='teacher2', subject='bio', expirience=1)
# >>> teacher2.students.set((student1, student3))
# >>> teacher2.students.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (3)>]>
# >>> student1.teachers.all()
# <QuerySet [<Teacher: Teacher object (1)>, <Teacher: Teacher object (2)>]>
# >>> student_f = Student.objects.filter(age__gt=15)
# >>> student_f
# <QuerySet [<Student: Student object (2)>, <Student: Student object (3)>]>
# >>> from django.db.models import Avg
# >>> student_age = Student.objects.aggregate(Avg('age'))
# >>> student_age
# {'age__avg': 16.0}
# >>> total_exp = sum(teacher.expirience for teacher in Teacher.objects.all())
# >>> total_exp
# 3