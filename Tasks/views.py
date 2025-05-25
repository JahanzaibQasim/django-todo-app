from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class TaskListView(LoginRequiredMixin,ListView):
    login_url = 'login_view'
    redirect_field_name = 'next'
    model = Task
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user, complete=False)
        context['completed_tasks'] = Task.objects.filter(user=self.request.user, complete=True)
        return context

class CreateTaskView(LoginRequiredMixin, CreateView):
    login_url = 'login_view'
    model = Task
    template_name= 'create_tasks.html'
    fields= ['title', 'description']
    success_url = reverse_lazy('tasks_list')  # Redirect to tasks list after form submission

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the task
        return super().form_valid(form)

@login_required(login_url='login_view')
def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Add user filter
    task.complete = True
    task.save()
    return redirect('tasks_list')

@login_required(login_url='login_view')
def mark_incomplete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Add user filter
    task.complete = False
    task.save()
    return redirect('tasks_list')

class EditTaskView(LoginRequiredMixin, UpdateView):
    login_url = 'login_view'
    model = Task
    template_name= 'create_tasks.html'
    fields= ['title', 'description']
    success_url = reverse_lazy('tasks_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    login_url = 'login_view'
    model = Task
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('tasks_list')
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('tasks_list')
            else:
                return redirect('login_view')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('tasks_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login_view')