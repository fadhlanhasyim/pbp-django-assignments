from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskForm
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'data_todolist':data_todolist,
        'nama':request.user,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    task = TaskForm()

    if request.method == "POST":
        task = TaskForm(request.POST)
        if task.is_valid():
            title = task.cleaned_data['title']
            description = task.cleaned_data['description']
            Task.objects.create(title=title, description=description, user=request.user, date=datetime.date.today())
            return redirect('todolist:show_todolist')
    
    context = {'task':task}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login')
def delete_task(request, id):
    task = get_object_or_404(Task, id = id)
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login')
def update_task(request, id):
    task = get_object_or_404(Task, id = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response