from django.shortcuts import render, reverse

# Create your views here.


from .models import Articles
from .serializers import ArticleSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from first.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from first.serializers import UserSerializer
from rest_framework.decorators import api_view


class ArticleAPIViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
    })
