from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

    def __str__(self):
        return self.email
