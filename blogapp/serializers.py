from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from .models import Card, PostView, Comment, Like
from django.utils.timesince import timesince #timestamp için kullanılacak

#! Auth Serializers

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True, required=True, validators=[validate_password], style={"input_type":"password"})
    password2 = serializers.CharField(write_only = True, required=True, validators=[validate_password], style={"input_type":"password"})
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'          
        ]
        
    def create(self, validated_data):
        # print('validated_data: ', validated_data)
        password = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        # print('user: ', user)
        user.set_password(password)
        user.save()
        return user
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password' : "Password fields didn't match."})
        return data

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')
        
class CardSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    class Meta:
        model = Card
        fields = ['id', 'user', 'user_id', 'title', 'image_url', 'content', 'createdDate', 'updatedDate']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
        