from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomObjectManager(BaseUserManager):
    def create_user(self, email, username, firstname, password, **other_fields):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            raise ValueError("users must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, firstname, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff = True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser = True')
        
        return self.create_user(email, username, firstname, password, **other_fields)
        

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", unique=True)
    username = models.CharField(max_length=150, unique = True)
    firstname = models.CharField(verbose_name="first name", max_length=150, blank=True)
    startdate = models.DateTimeField(verbose_name="start date", auto_now_add=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomObjectManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname']

    def __str__(self):
        return self.username

