from rest_framework.serializers import ModelSerializer

from app.models import User

class UserSerializer(ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['avatar'] = instance.avatar.url
        return data

    class Meta:
        model = User
        fields = '__all__'