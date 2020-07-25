from django.db import models
from django.db.models import ForeignKey



class Semester(models.Model):
    semester = models.CharField(max_length=5)

    def __str__(self):
        return self.semester


class Department(models.Model):
    dept = [('CSE', 'CSE'), ('ECE', 'ECE'),
            ('EEE', 'EEE'), ('CE', 'CE'), ]

    department = models.CharField(max_length=3, choices=dept)

    def __str__(self):
        return self.department


class StudentFormModel(models.Model):

    department = models.ForeignKey('baseapp.Department',
                                   on_delete=models.CASCADE)
    acctype = [('Student', 'Student'), ('Faculty', 'Faculty'), ]
    account = models.CharField(max_length=7, choices=acctype, default='')
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150, primary_key=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return '{} {}, {}'.format(self.first_name, self.last_name, self.department)


class FacultyFormModel(models.Model):

    department = models.ForeignKey('baseapp.Department',
                                   on_delete=models.CASCADE)
    acctype = [('Student', 'Student'), ('Faculty', 'Faculty'), ]
    account = models.CharField(max_length=7, choices=acctype, default='')
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return '{} {}, {}'.format(self.first_name, self.last_name, self.department)


class StudentUpdateMarksModel(models.Model):
    sem = models.ForeignKey('baseapp.Semester', on_delete=models.CASCADE)
    name = models.ForeignKey('baseapp.StudentFormModel',
                             on_delete=models.CASCADE)

    subject_1 = models.IntegerField()
    subject_2 = models.IntegerField()
    subject_3 = models.IntegerField()
    subject_4 = models.IntegerField()

    def __str__(self):
        return '{}, sem: {}'.format(self.name, self.sem)


