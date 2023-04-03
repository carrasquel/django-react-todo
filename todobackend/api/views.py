from rest_framework import generics
from api.serializers import TodoSerializer
from todo.models import Todo


class TodoList(generics.ListAPIView):

    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('created')