from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import api, UserViewset

router = routers.SimpleRouter()

router.register("user", UserViewset, basename="user")

urlpatterns = [
    path("", api, name="api"),
    path("", include(router.urls)),
]

# Returns JSON when adding *.json suffix to URL
urlpatterns = format_suffix_patterns(urlpatterns)
