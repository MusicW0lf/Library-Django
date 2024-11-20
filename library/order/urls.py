

from django.urls import path, include
from . import views

urlpatterns = [
   # path('delete/<int:id>', views.order_delete, name = 'order_delete'),
   # path('create/', views.order_create, name='order_create'),
    path('', views.show_all, name='order_show_all'),

#<int:id>
]
