from django.urls import path
from .views import task_list, add_task, remove_task, complete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('remove/<int:task_id>/', remove_task, name='remove_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
]