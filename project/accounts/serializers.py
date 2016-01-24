from rest_framework import serializers
from project.accounts.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ('avatar', 'is_active',)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data['password'])
            instance.save()
            del validated_data['password']
        return super(UserProfileSerializer, self).update(instance, validated_data)
