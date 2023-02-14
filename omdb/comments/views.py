from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets

from comments.permissions import IsAuthorOrAdmin
from comments.serializers import CommentSerializer
from episodes.models import Episode

from comments.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.prefetch_related('user', 'episode').all()

    def get_permissions(self):
        permission_classes = (permissions.AllowAny, )
        if self.action == 'create':
            permission_classes = (permissions.IsAuthenticated, )
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = (permissions.IsAuthenticated, IsAuthorOrAdmin)

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        episode_obj = Episode.objects.get(pk=self.request.data.get('episode'))
        serializer.save(user=self.request.user, episode=episode_obj)
