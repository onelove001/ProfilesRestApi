from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status


class HelloApiView(APIView):
    """ Test Api View """

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of api features """

        api_data = [
            "Uses http methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django view",
            "Gives you the most control over you application logic",
            "Is mapped manually to URLs"
        ]

        return Response({"message": "Hello", "api_view": api_data})


    def post(self, request):
        """ Create a hello message with a Name """

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """ Handles updating an object """

        return Response({"message": "PUT"})


    def patch(self, request, pk=None):
        """ Handles updating an object """

        return Response({"message": "PATCH"})


    def delete(self, request, pk=None):
        """ Handles deleting of an object """
        
        return Response({"message": "DELETE"}) 

        