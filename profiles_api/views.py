from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = {
            "Uses HTTP methods as function (get, post, patch, put, delete)"
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        }

        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self,  request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'Put'})

    def patch(self, request):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an obeject"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Return a hello message"""

        a_viewSet = [
            '1',
            '2',
            '3',
        ]
        return Response({"a_viewSet" : a_viewSet})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        """getting an object by its id"""
        return Response({'http_method': 'Get'})

    def update(self, request, pk=None):
        """updating an object"""
        return Response({'http_method': 'put'})

    def partial_update(self, request, pk=None):
        """updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """removing an object"""
        return Response({'http_method': 'DELETE'})
