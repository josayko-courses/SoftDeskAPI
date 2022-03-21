from django.urls import include, path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import UsersViewset, ProjectsViewset, ContributorsViewset

urlpatterns = [
    # 3 - GET /projects/
    # 4 - POST /projects/
    path(
        "projects/",
        ProjectsViewset.as_view({"get": "list", "post": "create"}),
    ),
    # 5 - GET /projects/{id}/
    # 6 - PUT /projects/{id}/
    # 7 - DELETE /projects/{id}/
    path(
        "projects/<pk>/",
        ProjectsViewset.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    # 8 - POST /projects/{id}/users/
    # 9 - GET /projects/{id}/users/
    path(
        "projects/<project_id>/users/",
        ContributorsViewset.as_view({"get": "list", "post": "create"}),
    ),
    # 10 - DELETE /projects/{id}/users/
    path(
        "projects/<project_id>/users/<user_id>",
        ContributorsViewset.as_view({"delete": "destroy"}),
    ),
]

# Returns JSON when adding *.json suffix to URL
urlpatterns = format_suffix_patterns(urlpatterns)
