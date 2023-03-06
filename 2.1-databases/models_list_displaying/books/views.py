from datetime import datetime, date
from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'

    books_object = list(Book.objects.values())
    for i in books_object:
        i['pub_date'] = i['pub_date'].strftime('%Y-%m-%d')
    context = {'books': books_object}
    return render(request, template, context)

def date_view(request, pub_date):
    template = 'books/book.html'
    books_object = list(Book.objects.values())
    for i in books_object:
        i['pub_date'] = i['pub_date'].strftime('%Y-%m-%d')
    paginator = Paginator(books_object, 1)
    page = paginator.get_page(pub_date)
    context= {'books': [i for i in books_object if i['pub_date'] == pub_date],
             'page': page}
    return render(request, template, context)