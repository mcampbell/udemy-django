# Register your models here.
from django.contrib import admin

from .models import Author, Tag, Post

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
