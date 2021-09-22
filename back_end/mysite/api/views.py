from rest_framework import generics

from .serializers import TimeEntrySerializer, JobSerializer
from work_tracker.models import TimeEntry, Job
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class TimeEntryList(generics.ListCreateAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer


class TimeEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer
