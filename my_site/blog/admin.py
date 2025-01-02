# Register your models here.
from django.contrib import admin

from .models import Author, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author")
    list_filter = ("author", "date", "tags")
    prepopulated_fields = {"slug": ("title",)} # slug depends on title, and it's a slug field so will autoslugify



admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
