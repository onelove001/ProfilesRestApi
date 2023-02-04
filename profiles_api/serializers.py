from rest_framework import serializers
from profiles_api.models import *


class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our API View """

    name = serializers.CharField(max_length = 10)



class ProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = UserProfile
        fields = ("id", "email", "first_name", "last_name", "password")
        extra_kwargs = { 
            "password": {
                "write_only":True,
                "style": { "input": "password"}
            }
        }


    def create(self, validated_data):
        """ creates a new user and return """

        email = validated_data["email"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]

        user = UserProfile.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
        return user


    def update(self, instance, validated_data):
        """Handle updating user account"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)



