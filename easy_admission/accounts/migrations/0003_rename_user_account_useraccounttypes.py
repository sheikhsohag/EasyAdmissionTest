# Generated by Django 5.0.4 on 2024-05-08 11:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_account_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Account',
            new_name='UserAccountTypes',
        ),
    ]
