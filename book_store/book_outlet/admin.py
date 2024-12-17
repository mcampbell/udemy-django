
from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)

