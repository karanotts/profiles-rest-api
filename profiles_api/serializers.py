""" Serializers allow to convert data inputs into python objects and other way around """

from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing APIView """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True, # can't read (GET, RETRIEVE) object, so can't read password
                'style': {'input_type': 'password'} # this will star **** password so it's not visible when being written to browser
            }
        }


    def create(self, validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


    def update(self, instance, validated_data):
        """ Update user account """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)