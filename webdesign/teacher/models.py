from django.db import models

# Create your models here.
class Teacher(models.Model):
    tname = models.CharField(max_length=250)
    tdepartment = models.EmailField(max_length=250)
    tcourse = models.CharField(max_length=250)
    tsubject = models.CharField(max_length=250)
    class Meta:
        db_table = "teacher"