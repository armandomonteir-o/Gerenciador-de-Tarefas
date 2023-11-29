from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    priority = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    deadline = deadline = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
