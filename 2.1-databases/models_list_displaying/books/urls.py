from django.urls import path

from books.views import books_view, books_paginator_view


urlpatterns = [
    path('', books_view, name='books'),
    path('<date:pub_date>/', books_paginator_view, name='books_paginator'),
]