from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from .models import Book


def index(request):
    def by_title(book):
        return book.title

    books_qs = Book.objects.all()
    all_books = sorted(books_qs, key=lambda book: book.title)
    # or all_books = books_qs.order_by("title")
    count = books_qs.count() # or len(all_books)
    average_rating = books_qs.aggregate(Avg("rating"))["rating__avg"]
    return render(request, "book_outlet/index.html", {
        "books": all_books,
        "count": count,
        "average_rating": average_rating
    })


def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404("Book not found")

    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html", {"book": book})

def book_detail_by_slug(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {"book": book})
