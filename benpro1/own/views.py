from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


def home(request):
    Tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': Tasks
    }
    return render(request, 'HTML/home.html', context)


def add_Task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home_page')

# def home(request):
#     tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
#     completed_tasks = Task.objects.filter(
#         is_completed=True).order_by('-created_at')
#     context = {
#         'tasks': tasks,
#         'completed_tasks': completed_tasks
#     }
#     return render(request, 'HTML/home.html', context)


# def addTask(request):
#     if request.method == 'POST':
#         task = request.POST.get('task')
#         if task:
#             Task.objects.create(task=task)
#     return redirect('home_page')


# def mark_as_done(request, pk):
#     task = Task.objects.get(id=pk)
#     task.is_completed = True
#     task.save()
#     return redirect('home_page')


# def mark_as_undone(request, pk):
#     task = Task.objects.get(id=pk)
#     task.is_completed = False
#     task.save()
#     return redirect('home_page')


# def delete_task(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return redirect('home_page')


# def edit_task(request, pk):
#     task = Task.objects.get(id=pk)
#     if request.method == 'POST':
#         new_task = request.POST.get('task')
#         if new_task:
#             task.task = new_task
#             task.save()
#         return redirect('home_page')
#     context = {'task': task}
#     return render(request, 'HTML/edit_task.html', context)
# Create your views here.
# def home(request):
#     return HttpResponse('homepage')
