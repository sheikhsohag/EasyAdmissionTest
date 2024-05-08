from django.contrib.auth.models import AbstractUser, User
from django.db import models

type =[
    ('student', 'Student'), 
    ('teacher', 'Teacher')
    ]


class UserAccountTypes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=type)
    

    def __str__(self):
        return self.user.username

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    subdistrict = models.CharField(max_length=40)
    district = models.CharField(max_length=50)
    ssc_board = models.CharField(max_length=40)
    ssc_year = models.IntegerField()
    ssc_result = models.FloatField()
    hsc_board = models.CharField(max_length=40)
    hsc_year = models.IntegerField()
    hsc_result = models.FloatField()

class TeacherProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cur_village = models.CharField(max_length=50)
    cur_subdistrict = models.CharField(max_length=40)
    cur_district = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    subdistrict = models.CharField(max_length=40)
    district = models.CharField(max_length=50)
    phd = models.BooleanField()
    dept = models.CharField(max_length=200)
    title = models.CharField(max_length=50)




