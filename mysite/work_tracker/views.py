from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from .models import TimeSheet, Job
from .forms import TimeSheetQuote


# Create your views here.
def index(request):
    return render(request, "work_tracker/index.html")


def time_sheet_list(request):
    time_sheets = TimeSheet.objects.all()
    return render(
        request, "work_tracker/time_sheet_list.html", {"time_sheets": time_sheets}
    )


def entry_detail(request, pk):
    entry = get_object_or_404(TimeSheet, pk=pk)
    return render(request, "work_tracker/entry_detail.html", {"entry": entry})


def job_detail(request):
    # details = get_object_or_404(Job, pk=1)
    return render(request, "work_tracker/job_detail.html")


def entry_new(request):
    pass


def entry_edit(request, pk):
    pass


def entry_delete(request, pk):
    pass
