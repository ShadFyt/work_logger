from .forms import MyCustomUserForm
from django.urls import path, include
from django_registration.views import RegistrationView
from django.contrib.auth import views as auth_views

from . import views

app_name = "work_tracker"
urlpatterns = [
    path("", views.TimeEntryListView.as_view(), name="time_entry_list"),
    path("<int:pk>", views.TimeEntryDetailView.as_view(), name="entry-datail"),
    path("entry/new/", views.TimeEntryCreate.as_view(), name="entry-new"),
    path("<int:pk>/update", views.TimeEntryUpdateView.as_view(), name="entry-update"),
    path("<int:pk>/delete", views.TimeEntryDelView.as_view(), name="entry_delete"),
    path("job/<int:pk>", views.JobDetailView.as_view(), name="job_detail"),
    #path('accounts/register/', RegistrationView.as_view(form_class=MyCustomUserForm), name='django_registration_register'),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #path("accounts/", include('django_registration.backends.activation.urls')),
    #path("accounts/", include('django.contrib.auth.urls')),


]
