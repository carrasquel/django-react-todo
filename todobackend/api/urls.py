from django.urls import path
from api import views


urlpatterns = [
    path('todos/', views.TodoListCreateView.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroyView.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleCompleteView.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),
]