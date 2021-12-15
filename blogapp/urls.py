from django.urls import path, include
from .views import Register, Card_Crud, LikeView, View, CommentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cards', Card_Crud)
router.register('liked', LikeView)
router.register('comments', CommentView)

urlpatterns = [
    path('auth_login/', include('dj_rest_auth.urls')),
    path('register/', Register.as_view()),
    path('viewed/', View.as_view()),
    path('',  include(router.urls)),
]   
