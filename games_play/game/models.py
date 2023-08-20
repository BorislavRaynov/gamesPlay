from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Game(models.Model):
    CHOISES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("BoardCard Game", "Board/Card Game"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=15, choices=CHOISES)
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
    max_level = models.IntegerField(validators=[MinValueValidator(1)], blank=False, null=False)
    image = models.URLField()
    summary = models.TextField(null=False, blank=False)
