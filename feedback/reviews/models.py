from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Review(models.Model):
    # Probably best to ensure length/etc validations on these match the html view

    username = models.CharField(max_length=100, null=False)
    review = models.TextField(max_length=200, null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=False
    )

    def __str__(self):
        return f"{self.username} rated us {self.rating} stars."
