from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', include(router.urls)),
    path('login/', views.LoginView, name='login'),
]
