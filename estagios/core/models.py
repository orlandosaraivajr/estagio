from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)

class TimeStampedModel(models.Model):
    criado_em = models.DateTimeField(
        verbose_name='criado em',
        auto_now_add=True,
        auto_now=False
    )
    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True