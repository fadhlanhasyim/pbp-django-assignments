from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task, delete_task, update_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('<id>/delete/', delete_task, name='delete-task'),
    path('<id>/update/', update_task, name='update-task'),
]