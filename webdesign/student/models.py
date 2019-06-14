from django.db import models
from django.forms import forms
# department= [
#     ('enginnering', 'Enginnering'),
#     ('bsc', 'Bsc'),
#    ]
# cources= [
#     ('mech_enginnering', 'Mech_Enginnering'),
#     ('Comp_enginnering', 'Comp_Enginnering'),
# ('bsc_comp', 'Bsc_comp'),
# ('bsc_math', 'Bsc_math')
# ]
# roles= [
#     ('teacher', 'Teacher'),
#     ('parent', 'Parent'),
# ('student', 'Student'),
# ]
class Student(models.Model):
    eid = models.CharField(max_length=250)
    eemail = models.EmailField()
    epassword = models.CharField(max_length=250)
    ename = models.CharField(max_length=250)
    econtact = models.CharField(max_length=150)
    edepartment = models.CharField(max_length=150)
    ecources = models.CharField(max_length=150)
    eroles = models.CharField(max_length=150)
    # edepartment= models.CharField(label='Choose your department', widget=models.Select(choices=department))
    # ecources= models.CharField(label='Choose your cources', widget=models.Select(choices=cources))
    # eroles= models.CharField(label='Choose your role', widget=models.Select(choices=roles))
    class Meta:
        db_table = "student"
