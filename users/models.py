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