from django.urls import path
from api import views


urlpatterns = [
    path("todos/", views.TodoListCreateView.as_view()),
    path("todos/<int:pk>", views.TodoRetrieveUpdateDestroyView.as_view()),
    path("todos/<int:pk>/complete", views.TodoToggleCompleteView.as_view()),
    path("signup/", views.SignUpView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
]
