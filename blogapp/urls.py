from django.urls import path, include
from .views import Register, Card_Crud, LikeView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cards', Card_Crud)

urlpatterns = [
    path('auth_login/', include('dj_rest_auth.urls')),
    path('register/', Register.as_view()),
    path('liked/<int:pk>', LikeView.as_view()),
    path('',  include(router.urls)),
]   
