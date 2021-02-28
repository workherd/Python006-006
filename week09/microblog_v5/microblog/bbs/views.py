from django.shortcuts import render, reverse

# Create your views here.


from .models import Articles, Posts, UserScore
# from .models import UserProfile
from .serializers import ArticleSerializer, UserSerializer, CreateUserSerializer, PostsSerializer
# from .serializers import  ProfileSerializer
from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from bbs.permissions import IsOwnerOrReadOnly
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.decorators import api_view
from rest_framework import filters
from django_filters import rest_framework as rf_filters
from .filters import ArticlesFilters
from rest_framework import serializers
from notifications.signals import notify
from django.forms.models import model_to_dict


class CreateUserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        # 序列化
        serializer = self.get_serializer(user)
        data = serializer.data
        del data['password']
        return Response(data)

    def list(self, request: Request, *args, **kwargs):
        """ 获取用户列表 """
        return Response([])

    def create(self, request, *args, **kwargs):
        """ 创建用户 """
        serializer = CreateUserSerializer(data=request.data, context={'request': request})
        # print(request.data['username'])
        # save 前必须先调用 is_valid()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def update(self, request: Request, *args, **kwargs):
    #     """
    #     更新用户信息
    #     """

    # def destroy(self, request: Request, *args, **kwargs):
    #     """
    #     删除用户
    #     """
    #     serializer = self.get_serializer(self.queryset, many=True)
    #     return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        查看用户视图
        """
    # url = serializers.HyperlinkedIdentityField(view_name="myapp:user-detail")

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """ 用户详情 """
        # 获取实例
        user = self.get_object()

        serializer = self.get_serializer(user)
        data = serializer.data

        # 接收通知
        user_notify = User.objects.get(pk=user.pk)
        # notify_dict = model_to_dict(user_notify.notifications.unread().first(), fields=["verb",])

        new_dict = {}
        for obj in user_notify.notifications.unread():
            notify_dict = model_to_dict(obj, fields=["verb",])
            new_dict.setdefault("verb", []).append(notify_dict["verb"])
            # dict(data, **notify_dict)

        return Response(dict(data, **new_dict))

    # def list(self, request: Request, *args, **kwargs):
        #     """ 获取用户列表 """


class ArticlesAPIViewSet(viewsets.ModelViewSet):
    """
        文章视图
        """
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = (rf_filters.DjangoFilterBackend, filters.SearchFilter,)

    # 增加Django搜索功能,建议使用DRF集成的FilterSet替代
    # https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html#quickstart
    # filter_fields = ('content',)
    filter_class = ArticlesFilters
    search_fields = ['title', 'body']

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)


# class UserProfileViewSet(viewsets.ModelViewSet):
#
#     queryset = UserProfile.objects.all()
#     serializer_class = ProfileSerializer
#
#     def retrieve(self, request, pk=None):
#         """ 用户详情 """
#         # 获取实例
#         userprofile = self.get_object()
#
#         # 序列化
#         serializer = self.get_serializer(userprofile)
#         return Response(serializer)
#
#     def list(self, request: Request, *args, **kwargs):
#         """ 获取用户详细信息 """
#         return Response([])
#
#     def create(self, request, *args, **kwargs):
#         """ 创建用户 """
#         serializer = ProfileSerializer(data=request.data, context={'request': request})
#         # print(request.data['username']
#         # save 前必须先调用 is_valid()
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


class UserPostsAPIViewSet(viewsets.ModelViewSet):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    # def retrieve(self, request, pk=None):
    #     """ 用户详情 """
    #     # 获取实例
    #     postsall = self.get_object()

    #     # 序列化
    #     serializer = self.get_serializer(postsall)
    #     return Response(serializer)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 发送用户
        user_id = serializer.data["user_id"]
        user = User.objects.get(pk=user_id)

        # 接收用户
        recipient_id = serializer.data["article_id"]
        recipient_user = Articles.objects.filter(id=recipient_id).values('author_id').first()['author_id']
        recipient = User.objects.get(pk=recipient_user)

        # 通知内容
        posts_content = serializer.data["content"]

        # 发送通知
        notify.send(user, recipient=recipient, verb = posts_content)

        return Response(serializer.data)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-detail', request=request, format=format),
        'createusers': reverse('create-user', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format),
        'posts': reverse('posts-list', request=request, format=format),
    })