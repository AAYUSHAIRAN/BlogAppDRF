from rest_framework import serializers
from .models import Article
from users.models import NewUser

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['email', 'username', 'firstname', 'password']
    def create(self, validated_data):
        user = NewUser.objects.create_user(validated_data['email'],  validated_data['username'], validated_data['firstname'], validated_data['password'])
        return user


    