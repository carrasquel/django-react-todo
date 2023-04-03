from rest_framework import generics, permissions
from api.serializers import TodoSerializer
from todo.models import Todo


class TodoListCreateView(generics.ListCreateAPIView):

    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
