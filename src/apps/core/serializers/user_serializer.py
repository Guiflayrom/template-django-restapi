from rest_framework import serializers

from src.apps.core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'], username=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = User.objects.get(email=validated_data['email'])
        user.email = validated_data['email']
        user.username = validated_data['email']

        user.set_password(validated_data['password'])
        user.save()
        return user
