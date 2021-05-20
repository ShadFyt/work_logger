from django.urls import path

from . import views

app_name = "work_tracker"
urlpatterns = [
    # path('index', views.index, name='index'),
    path("", views.TimeEntryListView.as_view(), name="time_sheet_list"),
    path("<int:pk>", views.TimeEntryDetailView.as_view(), name="entry_datail"),
    path("entry/new/", views.TimeEntryCreate.as_view(), name="entry-new"),
    path("<int:pk>/update", views.TimeEntryUpdateView.as_view(), name="entry-update"),
    path("<int:pk>/delete", views.TimeEntryDelView.as_view(), name="entry_delete"),
    path("job/<int:pk>", views.JobDetailView.as_view(), name="job_detail"),
]
