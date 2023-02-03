from django.urls import path
from profiles_api.views import *


app_name = "api"


urlpatterns = [
    path("hello-view/", HelloApiView.as_view(), name="Hello"),
]