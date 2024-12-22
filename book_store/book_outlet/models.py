from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Address(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return ", ".join([self.city, self.state])


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=True)
    last_name = models.CharField(max_length=100, null=False, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        ret = " ".join([self.first_name, self.last_name])
        if self.address:
            ret += f" ({self.address})"
        return ret.strip()


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # I don't like null-true here, but it's in Max's tutorial so we'll go with that for now.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def save(self, *args, **kwargs):
        # This also works, mostly.
        # self.slug = self.title.replace(" ", "-").lower()
        self.slug = slugify(self.title)
        super().save()
