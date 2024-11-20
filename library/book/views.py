from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q, Value
from django.http import HttpResponseForbidden
from django.db.models.functions import Concat
def search_books(filter_item):
    names = filter_item.split()
    q_objects = Q()

    for name in names:
        q_objects |= Q(authors__first_name__icontains=name) | Q(authors__last_name__icontains=name)

    q_objects |= Q(name__icontains=filter_item)

    books = Book.objects.filter(q_objects).distinct()
    return books

def book_list(request):
    query = request.GET.get('query', '').strip()

    books = Book.objects.all()

    if query:
        books = books.annotate(
            author_full_name=Concat('authors__name', Value(' '), 'authors__surname')
        )
    
        try:
            query_int = int(query)
            books = books.filter(
                Q(name__icontains=query) |
                Q(author_full_name__icontains=query) |
                Q(count=query_int)
            ).distinct()

        except ValueError:
            books = books.filter(
                Q(name__icontains=query) |
                Q(author_full_name__icontains=query)
            ).distinct()

    return render(request, 'book_list.html', {'books': books, 'query': query})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_details.html', {'book': book})

def user_books(request, user_id):
    role = request.session.get('role')
    if role != 1:
        return HttpResponseForbidden("You do not have permission to view this page.")
    books = Book.objects.filter(order__user_id=user_id)
    return render(request, 'book/user_books.html', {'books': books})
