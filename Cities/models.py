from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=150, default=None)
    state = models.CharField(max_length=150, default=None)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class UserRegister(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
