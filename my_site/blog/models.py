from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    # Normally this'd be a URL, but for simplicity, we're just using the image name which we'll assume to be in the
    # static folder
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    excerpt = models.TextField()  # could just be a longer CharField
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")
