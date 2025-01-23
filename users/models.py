from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.apps import apps
from core.utils.app_contants import default_created_on

class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is required.')
        if not username:
            raise ValueError('The Username field is required.')
        if not phone_number:
            raise ValueError('The Phone Number field is required.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_on = models.BigIntegerField(default=default_created_on)

    objects = UserManager()

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email', 'phone_number']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups', 
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions', 
        blank=True,
    )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Account = apps.get_model('accounts', 'Account')
        Account.objects.get_or_create(user=self)

    class Meta:
        db_table = 'users'