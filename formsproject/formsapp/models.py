from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    subjects_taught = models.CharField(max_length=200)


class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="group")


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    groups = models.ManyToManyField(Group, related_name="students_groups")
