from django.shortcuts import render
from library.models import Author, Book

# Create your views here.
def book_detail(request, pk):
    author_obj = Author.objects.get(pk=pk)
    book_objs = Book.objects.filter(writer_id=author_obj.id)
    context = {
        "libitems" : book_objs,
        "authors" : author_obj,
    }

    return render(request, "library/book_detail.html", context)

