from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from _helpers.db import TimeModel

CLIENT = "client"
ADMIN = "admin"

ACCOUNT_TYPE_CHOICES = (
    (CLIENT, "کاربر"),
    (ADMIN, "ادمین"),
)


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, account_type, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            account_type=account_type
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            account_type='admin'
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, TimeModel):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    account_type = models.CharField(default=CLIENT, choices=ACCOUNT_TYPE_CHOICES, max_length=10)
    username = models.CharField(max_length=30, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس ')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

    ACCOUNT_TYPES = tuple(dict(ACCOUNT_TYPE_CHOICES).keys())

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت‌ها'


class AccessToken(models.Model):
    token = models.CharField(max_length=256, default="")
    user = models.ForeignKey(to='account_management.Account', on_delete=models.CASCADE, primary_key=True)
    expire_time = models.DateTimeField(default=datetime.now() + timedelta(hours=2))
    account_type = models.CharField(default=CLIENT, choices=ACCOUNT_TYPE_CHOICES, max_length=10)
