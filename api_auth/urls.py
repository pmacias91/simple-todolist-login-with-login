from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'api_auth'

urlpatterns =[

    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
]