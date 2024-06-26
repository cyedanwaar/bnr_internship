from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, admin_or_staff=None):

        user = self.model(username=username, email=self.normalize_email(email), admin_or_staff=admin_or_staff)
        user.set_password(password)
        user.save()

        return user
    
    def create_staff(self, username, email, password, admin_or_staff=None):

        user = self.create_user(username, email, password, admin_or_staff)
        user.is_staff = True

        user.save()

        return user
    
    def create_admin(self, username, email, password=None, admin_or_staff=None):

        user = self.create_user(username, email, password, admin_or_staff)

        user.is_staff = True
        
        user.is_admin = True

        user.save()

        return user
    
    def create_superuser(self, username, email, password=None):

        user = self.create_user(username, email, password)

        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    class AdminOrStaff(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        NONE = "", ""

    username = models.CharField(max_length=100, unique=True, db_index=True, null=False)
    email = models.EmailField(max_length=100, unique=True, db_index=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    admin_or_staff = models.CharField(max_length=5, choices=AdminOrStaff.choices, null=True, blank=True, default=AdminOrStaff.NONE)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username
