from django.shortcuts import render
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Card, Like
from .serializers import CardSerializer, LikeSerializer
from .permissions import IsUserOrNotAllowed
from .pagination import NewPageNumberPagination

#!Auth views
class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"User successfully created."
        })
        
#! Drf view
class Card_Crud(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_class = IsUserOrNotAllowed
    pagination_class = NewPageNumberPagination
    
class LikeView(ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    