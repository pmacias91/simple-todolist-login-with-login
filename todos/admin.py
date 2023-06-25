from django.contrib import admin
from .models import *
# Register your models here.

class TodosAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "update_at", "isCompleted"]

admin.site.register(Todos, TodosAdmin)
