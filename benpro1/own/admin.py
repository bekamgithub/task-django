# Register your models here.
from django.contrib import admin
from .models import Task


class Taskadmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)


admin.site.register(Task, Taskadmin)
