from django.contrib import admin
from django.urls import path, include, re_path
from todos.views import *

app_name = 'todos'

urlpatterns =[
    re_path(r'^$', HomeView.as_view(), name="home"),

    path('todo-app/', TodoHomeView.as_view(), name="todo_app"),
    path('add/', addActivity, name='add_activity'),
    path('delete-activity/<int:id_activity>', deleteActivity, name='delete_activity'),
    path('update-activity/<int:id_activity>', updateActivity, name='update_activity'),

]
