from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home_page'),
    path('add/', views.add_Task, name='add_task'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit')

]


# urlpatterns = [
#     path('', views.home, name='home_page'),
#     path('addTask/', views.addTask, name='addTask'),
#     path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
#     path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
#     path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
#     path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

# ]
