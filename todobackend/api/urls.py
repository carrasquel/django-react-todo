from django.urls import path
from api import views


urlpatterns = [
    path('todos/', views.TodoList.as_view()),
]