from django.shortcuts import render
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    books_data = Book.objects.all()
    context = {'books': books_data}
    return render(request, template, context)
def books_pub(request, pub_date):
    template = 'books/books_pagi.html'
    book_pub = Book.objects.filter(pub_date = pub_date)[0]
    context = {'books': books_data}
    # return render(request, template, context)
    pass