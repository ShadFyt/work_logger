from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    template_name = "entry_detail.html"

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
    form_class = TimeEntryForm
    success_url = reverse_lazy("work_tracker:time_entry_list")

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)


class TimeEntryUpdateView(UpdateView):
    model = TimeEntry
    template_name = "time_entry_form.htm"
    form_class = TimeEntryForm
    success_url = "/work_tracker"


class TimeEntryDelView(DeleteView):
    model = TimeEntry
    success_url = "/work_tracker"
