# Generated by Django 5.0.6 on 2024-05-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_remove_applyinformation_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyinformation',
            name='transactions',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
