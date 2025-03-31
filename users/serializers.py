from rest_framework import serializers
from .models import UnihavenUser

class UnihavenUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnihavenUser
        fields = ['id', 'username', 'password', 'email', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UnihavenUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        return user