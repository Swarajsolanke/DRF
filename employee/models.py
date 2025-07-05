from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    add=models.CharField(max_length=20)
    salary=models.IntegerField()

    def __str__(self):
        return self.name,self.emp_id