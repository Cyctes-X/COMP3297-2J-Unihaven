from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UnihavenUser

# Register the UnihavenUser model with the default UserAdmin
admin.site.register(UnihavenUser, UserAdmin)