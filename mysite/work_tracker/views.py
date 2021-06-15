from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TimeEntry, Job
from .forms import TimeEntryForm


# Create your views here.
def index(request):
    #TODO: Make this the HomePageView
    return render(request, "work_tracker/index.html")


class TimeEntryListView(LoginRequiredMixin, ListView):
    # View all time entry realted to login User
    model = TimeEntry
    template_name = "time_entry_list.html"
    login_url = "login"

    # Gets data only realted to signed in user
    def get_queryset(self):
        user = self.request.user
        return TimeEntry.objects.filter(employee=user)

    def get_time_entry_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class JobListView(ListView):

    model = Job
    template_name = "job_list_html"

    def get_job_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class TimeEntryDetailView(LoginRequiredMixin, DetailView):

    model = TimeEntry
    template_name = "entry_detail.html"
    login_url = "login"

    def get_context_data(self, **kwargs: Any):
        return super().get_context_data(**kwargs)


class JobDetailView(LoginRequiredMixin, DetailView):

    model = Job
    template_name = "job_detail.html"
    login_url = "login"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class TimeEntryCreate(CreateView):
    model = TimeEntry
    template_name = "time_entry_form.html"
    form_class = TimeEntryForm
    success_url = reverse_lazy("work_tracker:time_entry_list")

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class TimeEntryUpdateView(UpdateView):
    model = TimeEntry
    template_name = "time_entry_form.html"
    form_class = TimeEntryForm
    success_url = "/work_tracker"


class TimeEntryDelView(DeleteView):
    model = TimeEntry
    success_url = "/work_tracker"

#TODO: Add edit Profile view