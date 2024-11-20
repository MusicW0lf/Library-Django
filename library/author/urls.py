

from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/<int:id>', views.author_delete, name = 'author_delete'),
    path('create/', views.author_create, name='author_create'),
    path('', views.show_all, name='author_show_all'),

#<int:id>
]
