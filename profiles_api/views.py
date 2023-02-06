from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework import filters
from rest_framework import viewsets
from .models import *
from .permissions import *
from .serializers import HelloSerializer, ProfileSerializer, ProfileFeedSerializer




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


# View Sets

class HelloViewSet(viewsets.ViewSet):
    """Test API View Sets"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return a Hello Message"""

        viewset_data = [
            "First and Second",
            "Third and Fourth",
            "Fifth and Sixth"
        ]
        return Response({"message": "Hello", "viewset_data": viewset_data})

    
    def create(self, request):
        """Create a new Hello Message for view-set"""

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message":message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Create a new Hello Message for view-set"""

        return Response({"http_method": "GET"})

    
    def update(self, request, pk=None):
        """ Handles updating an object """

        return Response({"http_method": "PUT"})


    def partial_update(self, request, pk=None):
        """ Handles updating part an object """

        return Response({"http_method": "PATCH"})


    def destroy(self, request, pk=None):
        """ Handles deleting an object """

        return Response({"http_method": "DELETE"})



class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating a profile """

    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ("id", "first_name", "last_name", "email", )



class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading, deleting and updating """

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, UpdateOwnStatus)
    serializer_class = ProfileFeedSerializer
    queryset = ProfileFeeds.objects.all()

    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user """
        serializer.save(user_profile=self.request.user)
        




        