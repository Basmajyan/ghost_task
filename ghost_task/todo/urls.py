from django.contrib import admin
from django.urls import path, include
import todo.views as views

urlpatterns = [
    path('todo', views.TodoList.as_view()),
    path('todo/<int:id>', views.TodoView.as_view()),
    path('status', views.StatusList.as_view()),
    path('status/<int:id>', views.StatusView.as_view()),
]
