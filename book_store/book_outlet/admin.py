from django.contrib import admin

from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "author", "rating", "is_bestseller")
    list_filter = ("author", "rating", "is_bestseller")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "state")

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")



admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
