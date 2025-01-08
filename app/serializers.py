from rest_framework.serializers import ModelSerializer
from social_django.models import UserSocialAuth

from app.models import User


class UserSerializer(ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['avatar'] = instance.avatar.url

        user_social = UserSocialAuth.objects.filter(user_id = instance.id).first()
        data['provider'] = 'default'
        if user_social:
            data['provider'] = user_social.provider
        return data

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'avatar', 'is_staff', 'is_superuser', 'is_active', 'role']