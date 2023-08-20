from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class User(models.Model):
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(12)])
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    picture = models.URLField(null=False, blank=False)
