from django.urls import path, include
from profiles_api.views import *
from rest_framework.routers import DefaultRouter


app_name = "api"


router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")

urlpatterns = [
    path("hello-view/", HelloApiView.as_view(), name="Hello"),
    path("", include(router.urls)),
]