from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(is_deleted=False)
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['due_date']
    search_fields = ['title']

    @swagger_auto_schema(
        operation_description="Create a new task",
        responses={
            201: TaskSerializer,
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "errors": {
                            "title": ["This field is required."],
                            "description": ["This field is required."],
                            "due_date": ["This field is required."]
                        }
                    }
                }
            )
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the task'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the task'),
                'due_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Due date of the task'),
            },
            required=['title', 'description', 'due_date'],
            examples={
                "application/json": {
                    "title": "Comprar leite",
                    "description": "Comprar leite no supermercado",
                    "due_date": "2024-08-01"
                }
            }
        )
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Update an existing task",
        responses={
            200: TaskSerializer,
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "errors": {
                            "title": ["This field is required."],
                            "description": ["This field is required."],
                            "due_date": ["This field is required."]
                        }
                    }
                }
            )
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the task'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the task'),
                'due_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Due date of the task'),
            },
            required=['title', 'description', 'due_date'],
            examples={
                "application/json": {
                    "title": "Comprar leite",
                    "description": "Comprar leite no supermercado",
                    "due_date": "2024-08-01"
                }
            }
        )
    )
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a task",
        responses={
            200: openapi.Response(
                description="Task deleted successfully",
                examples={
                    "application/json": {
                        "detail": "Task deleted successfully"
                    }
                }
            )
        }
    )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'detail': 'Task deleted successfully'}, status=status.HTTP_200_OK)


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Register a new user",
        responses={
            201: openapi.Response(
                description="User created successfully",
                examples={
                    "application/json": {
                        "status": "User created successfully"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad Request",
                examples={
                    "application/json": {
                        "error": "All fields are required"
                    }
                }
            )
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
            },
            required=['username', 'password', 'email'],
            examples={
                "application/json": {
                    "username": "testuser",
                    "password": "password123",
                    "email": "testuser@example.com"
                }
            }
        ),
    )
    def post(self, request):
        data = request.data
        if not data.get('username') or not data.get('password') or not data.get('email'):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create(
                username=data['username'],
                password=make_password(data['password']),
                email=data['email']
            )
            return Response({'status': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
