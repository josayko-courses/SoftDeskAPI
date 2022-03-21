from django.urls import include, path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import UsersViewset, ProjectsViewset, ContributorsViewset, api

router = routers.SimpleRouter()

router.register("users", UsersViewset, basename="users")
router.register("projects", ProjectsViewset, basename="projects")
router.register("contributors", ContributorsViewset, basename="contributors")

urlpatterns = [
    path("", api, name="api"),
    path("", include(router.urls)),
]

# Returns JSON when adding *.json suffix to URL
urlpatterns = format_suffix_patterns(urlpatterns)
