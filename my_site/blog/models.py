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
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    excerpt = models.TextField()  # could just be a longer CharField
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")


# Comment model.  Every post can have multiple comments, but a comment can only belong to one post.
# A comment is also tied to the user that created it.
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateField(auto_now=True)
