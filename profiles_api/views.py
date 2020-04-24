""" Create your views here. """

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as functions (GET, POST, PATCH, PUT, DELETE)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ POST - handle creating an object """
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():   # is set to maxchar=10, so is valid if <=10char
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None): # pk - primary key of the object being updated
        """ PUT - handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ PATCH - handle partial updating an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ DELETE - handle deleting of an object """
        return Response({'method': 'DELETE'})