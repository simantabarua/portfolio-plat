from django.db import models
from .utils import UserManager
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# Create your models here.

class AdminUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin Users'

class User(AbstractBaseUser):
    PROFESSIONS = [
        ("doctor", "Doctor"),
        ("engineer", "Engineer"),
        ("teacher", "Teacher"),
        ("lawyer", "Lawyer"),
        ("artist", "Artist"),
        ("developer", "Developer"),
        ("business", "Businessperson"),
        ("other", "Other"),
    ]
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()
    profession = models.CharField(max_length=20, choices=PROFESSIONS)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
