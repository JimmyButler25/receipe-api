from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """create and save new user"""
        # normalize the email below
        user = self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user

# creating model class
class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """assign UserManager to User"""
    objects = UserManager()
    

    USERNAME_FIELD = 'email'














"""USERNAME_FIELD
A string describing the name of the field on the user model that is used as the unique identifier. This will
usually be a username of some kind, but it can also be an email address, or any other unique identifier. The
field must be unique (i.e., have unique=True set in its definition), unless you use a custom authentication
backend that can support non-unique usernames."""


"""  is_active
A boolean attribute that indicates whether the user is considered “active”. This attribute is provided as an
attribute on AbstractBaseUser defaulting to True. """