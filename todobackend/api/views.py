from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from api.serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by("-created")

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
        serializer.instance.completed = not (serializer.instance.completed)
        serializer.save()


class SignUpView:
    @classmethod
    def as_view(cls):
        return SignUpView.signup

    @classmethod
    @csrf_exempt
    def signup(cls, request):
        if request.method == "POST":
            try:
                data = JSONParser().parse(request)
                username = data["username"]
                password = data["password"]
                user = User.objects.create_user(username=username, password=password)
                user.save()

                token = Token.objects.create(user=user)

                return JsonResponse({"token": str(token)}, status=201)

            except IntegrityError:
                return JsonResponse(
                    {"error": "Username taken. Choose another username."}, 400
                )


class LoginView:
    @classmethod
    def as_view(cls):
        return LoginView.login

    @classmethod
    @csrf_exempt
    def login(cls, request):
        if request.method == "POST":
            data = JSONParser().parse(request)
            username = data["username"]
            password = data["password"]
            user = authenticate(request, username=username, password=password)

            if not user:
                return JsonResponse(
                    {"error": "unable to login. check username and password"},
                    status=400,
                )

            else:
                try:
                    token = Token.objects.get(user=user)
                except:
                    token = Token.objects.create(user=user)

                return JsonResponse({"token": str(token)}, status=201)


class LogoutView:
    permission_classes = [permissions.IsAuthenticated]

    @classmethod
    def as_view(cls):
        return LogoutView.logout

    @classmethod
    @csrf_exempt
    def logout(cls, request):
        if request.method == "POST":
            try:
                key = request.headers.get("Authorization").replace("Token ", "")
                token = Token.objects.get(key=key)
                token.delete()

                return JsonResponse({"response": "user logout"}, status=201)
            except:
                return JsonResponse({"error": "something went wrong"}, status=400)
