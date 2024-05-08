from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_Account


class User_accountAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_type',]

admin.site.register(User_Account, User_accountAdmin)




