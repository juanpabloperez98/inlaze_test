from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.

# MODEL USER


class User(AbstractBaseUser, PermissionsMixin):
    """Fields definition for User."""
    nickname = models.CharField(max_length=50, null=False, blank=False)
    names = models.CharField(max_length=50, null=False,
                             blank=False, default='')
    lastname = models.CharField(
        max_length=50, null=False, blank=False, default='')

    def get_full_name(self):
        return f"{self.names} {self.lastname}"

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    class Genere(models.IntegerChoices):
        """
        It defines the genere of users in the program
        """
        MALE = 0
        FAMALE = 1
    genere = models.SmallIntegerField(default=Genere.MALE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
    objects = UserManager()

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Fields that will not be used into current system
    username = None

    def __str__(self):
        return f"{self.pk} {self.get_full_name()}"

