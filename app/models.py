from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.CharField(max_length=10)
    name=models.CharField(max_length=11)
    email=models.EmailField(max_length=20)
    branch=models.CharField(max_length=14)

    def __str__(self):
        return self.name 