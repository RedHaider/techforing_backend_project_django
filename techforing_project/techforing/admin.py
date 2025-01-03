from django.contrib import admin

from .models import User, Comment, Project, ProjectMember, Task

# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)