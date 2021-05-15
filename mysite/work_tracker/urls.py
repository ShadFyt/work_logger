from django.urls import path

from . import views

app_name = "work_tracker"
urlpatterns = [
    # path('index', views.index, name='index'),
    path("", views.time_sheet_list, name="time_sheet_list"),
    path("<int:pk>", views.entry_detail, name="entry_datail"),
    path("new", views.entry_new, name="entry_new"),
    path("edit/<int:pk>", views.entry_edit, name="entry_edit"),
    path("delete/<int:pk>", views.entry_delete, name="entry_delete"),
    path("job/<int:id>", views.job_detail, name="job_detail"),
]
