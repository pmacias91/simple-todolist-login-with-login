from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from .models import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required

#authenticating users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  get_user

from django.http import HttpResponseRedirect


# Create your views here.

class HomeView(TemplateView):
    template_name = "todos/home.html"

#@login_required(redirect_field_name="todos:login")
class TodoHomeView(TemplateView):
    template_name = "todos/index.html"

    def get_context_data(self, **kwargs):
        context = super(TodoHomeView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            todos = Todos.objects.filter(user=user).order_by('isCompleted', '-update_at', '-created_at')
            context['todo_list'] = todos
        else:
            context['todo_list'] = "" 
        return context
    
def addActivity(request):
    title = request.POST['title']
    Todos.objects.create(title=title, user=request.user)

    return redirect('todos:todo_app')

def deleteActivity(request, id_activity):
    todo = get_object_or_404(Todos, pk=id_activity)
    todo.delete()

    return redirect('todos:todo_app')

def updateActivity(request, id_activity):
    todo = get_object_or_404(Todos, pk=id_activity)
    
    isCompleted = request.POST.get('isCompleted', False) # .get allows to provide an additional parameter of a default value which is returned if the key is not in the dictionary. In this case "False"
    if isCompleted == 'on':
        isCompleted = True

    todo.isCompleted = isCompleted
    todo.save()

    return redirect('todos:todo_app')

