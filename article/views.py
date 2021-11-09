from .models import Article
from .serializer import ArticleSerializer, UserSerializer
from users.models import NewUser
from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework import generics

# Create your views here.

class ArticleList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserList(generics.ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer