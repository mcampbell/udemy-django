from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    author = models.CharField(max_length=100, default="Unknown")
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"
