from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password, **extra_fields):
        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email,password, **extra_fields):
        return self._create_user(email, password,**extra_fields)
