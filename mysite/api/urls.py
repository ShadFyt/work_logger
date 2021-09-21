from django.urls import path

from .views import TimeEntryApiView

urlpatterns = [path("", TimeEntryApiView.as_view())]
