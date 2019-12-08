from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

# Extend baseuser admin
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


# register the user
admin.site.register(models.User, UserAdmin)