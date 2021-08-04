#from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework import viewsets
from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer
