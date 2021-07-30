#from django.shortcuts import render
from django.db.models import query
from rest_framework import generics, permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer