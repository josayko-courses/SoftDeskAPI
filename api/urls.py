from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api.views import (
    ProjectsViewset,
    ContributorsViewset,
    IssuesViewset,
    CommentsViewset,
)

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
    # 10 - DELETE /projects/{id}/users/{id}/
    path(
        "projects/<project_id>/users/<user_id>/",
        ContributorsViewset.as_view({"delete": "destroy"}),
    ),
    # 11 - GET /projects/{id}/issues/
    # 12 - POST /projects/{id}/issues/
    path(
        "projects/<project_id>/issues/",
        IssuesViewset.as_view({"get": "list", "post": "create"}),
    ),
    # 13 - PUT /projects/{id}/issues/{id}/
    # 14 - DELETE /projects/{id}/issues/{id}/
    path(
        "projects/<project_id>/issues/<issue_id>/",
        IssuesViewset.as_view({"put": "update", "delete": "destroy"}),
    ),
    # 15 - POST /projects/{id}/issues/{id}/comments/
    # 16 - GET /projects/{id}/issues/{id}/comments/
    path(
        "projects/<project_id>/issues/<issue_id>/comments/",
        CommentsViewset.as_view({"get": "list", "post": "create"}),
    ),
    # 17 - PUT /projects/{id}/issues/{id}/comments/{id}/
    # 18 - DELETE /projects/{id}/issues/{id}/comments/{id}/
    # 19 - GET /projects/{id}/issues/{id}/comments/{id}/
    path(
        "projects/<project_id>/issues/<issue_id>/comments/<comment_id>/",
        CommentsViewset.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]

# Returns JSON when adding *.json suffix to URL
urlpatterns = format_suffix_patterns(urlpatterns)
