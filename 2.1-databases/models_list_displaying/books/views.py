import json

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


books = Book.objects.all()


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context)


def books_paginator_view(request, pub_date):
    template = 'books/books_list_paginating.html'
    dates = [elem.pub_date for elem in books.order_by('pub_date').distinct('pub_date')]
    paginator = Paginator(dates, 1)
    curr_page_ind = dates.index(pub_date)
    page = paginator.get_page(curr_page_ind+1)
    neighbours = [-1, -1]
    if page.has_previous():
        neighbours[0] = dates[curr_page_ind - 1]
    if page.has_next():
        neighbours[1] = dates[curr_page_ind + 1]
    context = {
        'books': books,
        'pub_date': pub_date,
        'page': page,
        'dates': dates,
        'neighbours': neighbours,
    }
    return render(request, template, context)
