from typing import Any, Dict, List
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import TimeEntry, Job
from .forms import TimeEntryForm


# Create your views here.
def index(request):
    return render(request, "work_tracker/index.html")


class TimeEntryListView(ListView):

    model = TimeEntry
    template_name = "time_entry_list.html"

    def get_time_entry_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class TimeEntryDetailView(DetailView):

    model = TimeEntry
    template_name = "entry_detail.htm"

    def get_context_data(self, **kwargs: Any):
        return super().get_context_data(**kwargs)


class JobDetailView(DetailView):

    model = Job
    template_name = "job_detail.htm"

    def get(self, request, *args: Any, **kwargs: Any):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class TimeEntryCreate(CreateView):
    model = TimeEntry
    template_name = "time_entry_form.htm"
    fields = ["day_in_week", "date", "start_time", "end_time", "job"]
    success_url = "/work_tracker"


class TimeEntryUpdateView(UpdateView):
    model = TimeEntry
    template_name = "time_entry_form.htm"
    fields = ["day_in_week", "date", "start_time", "end_time", "job"]
    success_url = "/work_tracker"



class TimeEntryDelView(DeleteView):
    model = TimeEntry
    success_url = "/work_tracker"
