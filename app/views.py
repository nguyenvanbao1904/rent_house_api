from rest_framework import viewsets, generics, permissions
from django.shortcuts import render
from social_django.models import UserSocialAuth

from app.models import User
from app.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet, generics.ListAPIView):
    def get_permissions(self):
        return [permissions.IsAuthenticated()]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        for i in data.data:
            tmp = UserSocialAuth.objects.filter(user_id=i['id']).first()
            i['provider'] = 'default'
            if tmp:
                if i['id'] == tmp.user_id:
                    i['provider'] = tmp.provider
        return data

def LoginView(request):
    return render(request, 'login.html')

