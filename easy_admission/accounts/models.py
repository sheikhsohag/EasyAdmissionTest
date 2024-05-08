from django.contrib.auth.models import AbstractUser, User
from django.db import models

type =[
    ('student', 'Student'), 
    ('teacher', 'Teacher')
    ]


class User_Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=type)
    

    def __str__(self):
        return self.user.username