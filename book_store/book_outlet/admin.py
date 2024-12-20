
from django.contrib import admin

from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "author", "rating", "is_bestseller")
    list_filter = ("author", "rating", "is_bestseller")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
