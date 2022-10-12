from unicodedata import name
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('<id>/delete/', delete_task, name='delete-task'),
    path('<id>/update/', update_task, name='update-task'),
    path('json/', show_json, name='show_json'),
    path('delete/<id>', delete_task_ajax, name='delete-task-ajax'),
    path('add/', create_task_ajax, name='create-task-ajax'),
    path('update/<id>', update_task_ajax, name='update-task-ajax'),
]