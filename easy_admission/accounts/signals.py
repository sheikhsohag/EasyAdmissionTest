

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserAccountTypes

@receiver(post_save, sender=User)
def create_user_account_type(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        # Create a UserAccountTypes entry only for non-superusers
        UserAccountTypes.objects.create(user=instance, account_type='student')  # Default to 'student'
