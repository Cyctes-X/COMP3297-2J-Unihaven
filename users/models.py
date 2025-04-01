from django.contrib.auth.models import AbstractUser
from django.db import models

class UnihavenUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('STUDENT', 'HKU Member'),
        ('CEDARS', 'CEDARS Specialist'),
        ('OWNER', 'Property Owner'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='STUDENT')

    def __str__(self):
        return self.username

# from django.db.models.signals import post_migrate
# from django.contrib.auth.models import Group
# from django.apps import AppConfig


# def create_user_groups(sender, **kwargs):
#     groups = ['HKU member', 'CEDARS', 'property owner']
#     for group in groups:
#         Group.objects.get_or_create(name=group)


# class UsersConfig(AppConfig):
#     name = 'Users'

#     def ready(self):
#         post_migrate.connect(create_user_groups, sender=self)
