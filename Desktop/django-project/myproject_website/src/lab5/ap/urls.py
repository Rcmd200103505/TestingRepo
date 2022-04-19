from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='tasks'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('create', views.create_task, name='create_task'),
    path('check_task/<int:task_id>', views.check_task, name="check_task"),
    path('edit_task/<int:task_id>', views.edit_task, name="edit_task")
]