from django.urls import path
from .views import register, main_page, login_view, logout_view, user_detail, user_list

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_detail, name='user_detail'),
]