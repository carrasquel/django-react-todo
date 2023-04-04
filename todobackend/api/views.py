from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

from api.serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo


class TodoListCreateView(generics.ListCreateAPIView):

    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Todo.objects.filter(user=user)


class TodoToggleCompleteView(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.completed = not(serializer.instance.completed)
        serializer.save()


@csrf_exempt
def signup(request):

    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            username = data['username']
            password = data['password']
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.save()

            token = Token.objects.create(user=user)

            return JsonResponse({'token': str(token)}, status=201)
        
        except IntegrityError:
            return JsonResponse({'error': 'Username taken. Choose another username.'}, 400)


@csrf_exempt
def login(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if not user:
            return JsonResponse(
                {'error': 'unable to login. check username and password'},
                status=400
            )
        
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            
            return JsonResponse({'token': str(token)}, status=201)
