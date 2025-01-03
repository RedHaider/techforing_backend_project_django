from django.contrib import admin
from django.urls import path, include
from .views import hello_world , RegisterUserView, LoginUserView, UserDetailView, UserUpdateView , UserDeleteView, ProjectCreateView, ProjectUpdateView, ProjectListView, ProjectRetrieveView , ProjectDeleteView, TaskCreateView, TaskListView, TaskRetrieveView, TaskUpdateView, TaskDeleteView, CommentCreateView, CommentListView, CommentRetrieveView , CommentUpdateView, CommentDeleteView, ProjectMemberCreateView, ProjectMemberListView, ProjectMemberRetrieveView , ProjectMemberDeleteView, ProjectMemberUpdateView

urlpatterns = [
    path('',hello_world, name='hello_world' ),
    path ('api/users/register/', RegisterUserView.as_view() , name='register_user'),
    path('api/user/login/', LoginUserView.as_view(), name = 'login_user'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('api/users-update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('api/user-delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    #Project Routes
    path('api/projects/', ProjectListView.as_view() , name='project_list' ),
    path('api/project/create/', ProjectCreateView.as_view(), name = 'project_create'),
    path('api/project/<int:pk>/', ProjectRetrieveView.as_view(), name='project_record'),
    path('api/project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('api/projects/delete/<int:pk>/', ProjectDeleteView.as_view(), name= ';project_delete' ),

    #Task Routes
    path('api/task/create/', TaskCreateView.as_view(), name='create_task'),
    path('api/task/', TaskListView.as_view(), name='task_list'),
    path('api/task/<int:pk>/', TaskRetrieveView.as_view(), name='task_record'),
    path('api/task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('api/task/delete/<int:pk>/', TaskDeleteView.as_view(), name= 'task_delete' ),

    #Comment Routes
    path('api/comment/create/', CommentCreateView.as_view(), name = "comment_create"),
    path('api/comment/', CommentListView.as_view(), name='comment_list'),
    path('api/comment/<int:pk>/', CommentRetrieveView.as_view(), name='comment_record'),
    path('api/comment/update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('api/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name= 'comment_delete' ),

    #project members
    path('api/project/member/create/', ProjectMemberCreateView.as_view(), name = "poject_member_create"),
    path('api/project/member/', ProjectMemberListView.as_view(), name='poject_member_list'),
    path('api/project/member/<int:pk>/', ProjectMemberRetrieveView.as_view(), name='poject_member_record'),
    path('api/project/member/update/<int:pk>/', ProjectMemberUpdateView.as_view(), name='poject_member_update'),
    path('api/project/member/delete/<int:pk>/', ProjectMemberDeleteView.as_view(), name= 'poject_member_delete' ),
]
