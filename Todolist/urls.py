from django.urls import path
from Todolist import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('todolist/', views.todolist, name="todolist"),
    path('todolist/delete_task/<task_id>', views.delete_task, name="delete_task"),
    path('todolist/edit_task/<task_id>', views.edit_task, name="edit_task"),
    path('todolist/complete/<task_id>', views.complete_task, name="complete_task"),
    path('todolist/pending/<task_id>', views.pending_task, name="pending_task"),

    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
]