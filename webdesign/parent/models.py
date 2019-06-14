from django.db import models

# Create your models here.
class Parent(models.Model):
    pname = models.CharField(max_length=250)
    studentName = models.CharField(max_length=250)
    departmentname = models.CharField(max_length=250)
    coursename = models.CharField(max_length=250)
    class Meta:
        db_table = "parent"