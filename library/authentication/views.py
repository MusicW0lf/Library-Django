# views.py in the authentication app

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser
from django.db import IntegrityError
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        role = request.POST['role']
        try:
            user = CustomUser.objects.create_user(
                email=email, password=password,
                first_name=first_name, middle_name=middle_name, last_name=last_name,
                role=role
            )
            user = authenticate(request, email=email, password=password)
            login(request, user)
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            request.session['role'] = user.role
            return redirect('main_page')
        except IntegrityError:
            messages.error(request, 'This email is already in use. Please choose a different email.')

    return render(request, 'regist.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print("User logged in:", request.user)
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            request.session['role'] = user.role
            return redirect('main_page')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')


def main_page(request):
    user_id = request.session.get('user_id')
    user_email = request.session.get('email')
    role = request.session.get('role')

    if user_id is not None:
        user_info = {
            'id': user_id,
            'email': user_email,
            'role':role
        }
    else:
        user_info = None
    return render(request, 'main_page.html', {'user': user_info})


def logout_view(request):
    logout(request)
    return redirect('main_page')

def user_list(request):
    role = request.session.get('role')
    if role != 1:
        return HttpResponseForbidden("You do not have permission to view this page.")

    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, user_id):
    role = request.session.get('role')
    if role != 1:
        return HttpResponseForbidden("You do not have permission to view this page.")

    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_details.html', {'user': user})