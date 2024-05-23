from django.contrib.auth.models import AbstractUser, User
from django.db import models
import random

type =[
    ('student', 'Student'), 
    ('teacher', 'Teacher'),
    ('superuser', 'Superuser')
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
    registration = models.CharField(max_length=30)
    ssc_division = models.CharField(max_length=20)
    ssc_board = models.CharField(max_length=40)
    ssc_year = models.IntegerField()
    ssc_result = models.FloatField()
    hsc_board = models.CharField(max_length=40)
    hsc_division = models.CharField(max_length=20)
    hsc_year = models.IntegerField()
    hsc_result = models.FloatField()
    roll_number = models.IntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.roll_number:
            self.roll_number = self.generate_unique_roll_number()
        super().save(*args, **kwargs)

    def generate_unique_roll_number(self):
        min_roll_number = 100000
        max_roll_number = 999999
        roll_number = random.randint(min_roll_number, max_roll_number)
        while ProfileModel.objects.filter(roll_number=roll_number).exists():
            roll_number = random.randint(min_roll_number, max_roll_number)
        return roll_number

    def __str__(self):
        return self.full_name

   



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
    def __str__(self):
        return f"user {self.user.username} profile for Teacher"
    

class profileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    def __str__(self):
        return f"user {self.user.username}  user id {self.user.id}"




