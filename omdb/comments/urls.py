from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comments.views import CommentViewSet

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('comments/', comment_list, name='comment-list'),
    path('comments/<int:pk>/', comment_detail, name='comment-detail'),
]
