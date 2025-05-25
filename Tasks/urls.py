from .views import *
from django.urls import path
# from django.contrib.auth import views as auth_views


urlpatterns =  [
    path('', TaskListView.as_view(), name='tasks_list'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('mark-complete/<int:task_id>/', mark_complete, name='mark_complete'),
    path('mark-incomplete/<int:task_id>/', mark_incomplete, name='mark_incomplete'),
    path('edit/<int:pk>/', EditTaskView.as_view(), name='edit_task'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),   
]