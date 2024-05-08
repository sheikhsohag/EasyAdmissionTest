from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccountTypes, ProfileModel, TeacherProfileModel


class User_accountAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_type',]

admin.site.register(UserAccountTypes, User_accountAdmin)


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'father_name',]

admin.site.register(ProfileModel, ProfileModelAdmin)



class TeacherProfileModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phd',]

admin.site.register(TeacherProfileModel, TeacherProfileModelAdmin)




