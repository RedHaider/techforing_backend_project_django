from rest_framework import serializers
from .models import User , Project, Task, Comment, ProjectMember

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name', 'password']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Handle password separately
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Corrected 'isinstance' to 'instance'

        if password:
            instance.set_password(password)  # Corrected 'set_passowrd' to 'set_password'

        instance.save()
        return instance


    
class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','date_joined']

    def update(self, instance, validated_data):
        # Handle password separately
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Corrected 'isinstance' to 'instance'

        if password:
            instance.set_password(password)  # Corrected 'set_passowrd' to 'set_password'

        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','project_id','name', 'description','owner','created_at']
        read_only_fields = ['id','project_Id','created_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'priority',
            'assigned_to',
            'project',
            'created_at',
            'due_date'
        ]
        read_only_fields = ['id', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','user','task','created_at']
        read_only_fields = ['id','created_at','user']

class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = [ 'id','project','user','role' ]
        read_only_fields = ['id']
