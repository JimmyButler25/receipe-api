from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
""" converting strings to human readable text """
from django.utils.translation import gettext as _ 
from core import models 

# Extend baseuser admin
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        # we need to find the sections for the field set
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        # add important dates
        (_('Important dates'), {'fields': ('last_login',)})
    )

    # from django admin doc
    """ we need to customize filter to include our email, password """
    add_fieldsets = [
        # title of section
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2')
        }),
    ]
    # run the test


# register the user
admin.site.register(models.User, UserAdmin)