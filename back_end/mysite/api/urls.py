from django.urls import path
from django.urls.conf import include
from .views import TimeEntryList, TimeEntryDetail, JobList, JobDetail
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("", TimeEntryList.as_view()),
    path("<int:pk>", TimeEntryDetail.as_view()),
    path("job", JobList.as_view()),
    # path("job/<sqft>", JobDetail.as_view()),
    path("api-auth", include("rest_framework.urls")),
    path(
        "openapi",
        get_schema_view(title="Your Project", description="API for all things …"),
        name="openapi-schema",
    ),
]
