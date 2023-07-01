from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions'
    )

    def __str__(self):
        return '{}'.format(self.email)
