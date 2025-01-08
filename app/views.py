from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.shortcuts import render
from rest_framework.decorators import action

from app.models import User
from app.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["get"], detail=False, url_path="current-user", permission_classes=[permissions.IsAuthenticated])
    def get_current_user(self, request):
        user = request.user
        return Response(UserSerializer(user).data)
