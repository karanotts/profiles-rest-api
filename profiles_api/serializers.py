""" Serializers allow to convert data inputs into python objects and other way around """

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing APIView """
    name = serializers.CharField(max_length=10)