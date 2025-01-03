from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status
from .models import User, Project, Task, Comment, ProjectMember
from .serializers import RegisterSerializer, UserSerilaizer, ProjectSerializer, TaskSerializer, CommentSerializer, ProjectMemberSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.

def hello_world(request):
    return JsonResponse({"message":"Hello, World"})

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]  # This allows unauthenticated access


class LoginUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error":"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.check_password(password):
            return Response({"error":"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        })
    

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilaizer
    permission_classes = [IsAuthenticated]

########################################################
##################  Project ############################
########################################################
    
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Extract owner ID from the request data
        owner_id = self.request.data.get("owner")
        if not owner_id:
            raise ValueError("Owner ID is required to create a project.")
        
        # Assign the user as owner and save
        serializer.save(owner_id=owner_id)

class ProjectRetrieveView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the project instance
        self.perform_destroy(instance)  # Delete the instance
        return Response({"message": "Project deleted successfully."}, status=status.HTTP_200_OK)

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "List of tasks retrieved successfully",
            "data": serializer.data
        }, status= status.HTTP_200_OK)

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get project ID from the request payload
        project_id = self.request.data.get("project")
        if not project_id:
            raise ValueError("Project ID is required to create a task.")
        
        # Save task with the associated project
        serializer.save(project_id=project_id)

class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the project instance
        self.perform_destroy(instance)  # Delete the instance
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_200_OK)
    
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get task ID from the request payload
        task_id = self.request.data.get("task")
        if not task_id:
            raise ValueError("Task ID is required to create a comment.")

        # Save the comment with the associated task and user
        serializer.save(task_id=task_id, user=self.request.user)

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "List of Comments retrieved successfully",
            "data": serializer.data
        }, status= status.HTTP_200_OK)

class CommentRetrieveView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the project instance
        self.perform_destroy(instance)  # Delete the instance
        return Response({"message": "Comment deleted successfully."}, status=status.HTTP_200_OK)
    
class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class ProjectMemberCreateView(generics.CreateAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get project ID from the request payload
        project_id = self.request.data.get("project")
        if not project_id:
            raise ValidationError("Project ID is required to create a project member.")
        
        # Get user ID from the request payload
        user_id = self.request.data.get("user")
        if not user_id:
            raise ValidationError("User ID is required to create a project member.")
        
        # Ensure the user exists
        user = get_object_or_404(User, id=user_id)

        # Save the project member with the associated project and user
        serializer.save(project_id=project_id, user=user)

class ProjectMemberListView(generics.ListAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "List of Project Members retrieved successfully",
            "data": serializer.data
        }, status= status.HTTP_200_OK)

class ProjectMemberRetrieveView(generics.RetrieveAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]

class ProjectMemberDeleteView(generics.DestroyAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the project instance
        self.perform_destroy(instance)  # Delete the instance
        return Response({"message": "Project Member deleted successfully."}, status=status.HTTP_200_OK)
    
class ProjectMemberUpdateView(generics.UpdateAPIView):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]