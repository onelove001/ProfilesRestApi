from django.urls import path, include
from profiles_api.views import *
from rest_framework.routers import DefaultRouter


app_name = "api"


router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")
router.register("profile", UserProfileViewSet, basename="profile-viewset")
router.register("feeds", ProfileFeedViewSet, basename="profile-feed-viewset")

urlpatterns = [
    path("hello-view/", HelloApiView.as_view(), name="Hello"),
    path("login/", UserLoginApiView.as_view(), name="login"),
    path("", include(router.urls)),
]