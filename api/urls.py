from django.urls import include, path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import UserViewset, api

router = routers.SimpleRouter()

router.register("user", UserViewset, basename="user")

urlpatterns = [
    path("", api, name="api"),
    path("", include(router.urls)),
]

# Returns JSON when adding *.json suffix to URL
urlpatterns = format_suffix_patterns(urlpatterns)
