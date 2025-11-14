from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task


def home(request):
    Tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True)

    context = {
        'tasks': Tasks,
        'compl_task': completed_task
    }
    return render(request, 'HTML/home.html', context)


def add_Task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home_page')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = True
    task.save()
    return redirect('home_page')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = False
    task.save()
    return redirect('home_page')


def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home_page')


def edit(request, pk):
    get_task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home_page')
    else:
        context = {
            'get_task': get_task
        }

        return render(request, 'HTML/edit.html', context)


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
