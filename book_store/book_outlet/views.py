from django.shortcuts import render, get_object_or_404

from .models import Book


def index(request):
    def by_title(book):
        return book.title

    all_books = sorted(Book.objects.all(), key=lambda book: book.title)
    return render(request, "book_outlet/index.html", {"books": all_books})


def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404("Book not found")

    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html", {"book": book})
