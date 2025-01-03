from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import JsonResponse
from django.urls import path

class User(AbstractUser):
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    project_id = models.CharField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_project')
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_project_id(self):
        last_project = Project.objects.order_by('-id').first()
        if last_project:
            last_number = int(last_project.project_id[3:])
        else: 
            last_number = 0
        new_number = last_number + 1
        return f"PJT{new_number:09d}"

    def save(self, *args, **kwargs):
        if not self.project_id:
            self.project_id = self.generate_project_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_id

class ProjectMember(models.Model):
    ROLE_CHOICE = [
        ('admin','Admin'),
        ('member','Member'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_projects')
    role = models.CharField(max_length=255, choices= ROLE_CHOICE)


class Task(models.Model):
    STATUS_CHOICES = [
        ('to do','To Do'),
        ('in progress','In Progess'),
        ('done','Done'),
    ]
    PRIORITY_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='to do')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='medium')
    assigned_to = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'comments')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

