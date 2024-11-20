# Create your views here.
from .models import Author
from django.shortcuts import render, redirect


def show_all(request):
    context = {'author_list': Author.get_all()}
    return render(request, 'author_list.html',context)

def author_delete(request, id):
    author_t = Author.objects.get(pk=id)

    if len(author_t.books.all()) == 0:
        Author.delete_by_id(id)
    result = redirect('/author')
    return result
def author_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        patronymic = request.POST.get('patronymic', '')
        Author.create(name, surname, patronymic)
        result = redirect('/author')

    else:
        result = render(request, 'author_create.html')
    return result
