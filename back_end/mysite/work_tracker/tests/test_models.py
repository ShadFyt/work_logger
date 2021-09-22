from django.test import TestCase
from work_tracker.models import Job
from django.utils import timezone
from django.urls import reverse

# Job model test
class JobTest(TestCase):

    def create_job(
        self, name='lake view house', 
        job_type='sanding,',
        location='226 lakeview ave',
        sqft=2000
        ):
        return Job.objects.create(name=name, job_type=job_type, location=location,sqft=sqft)

    def test_job_creation(self):
        j = self.create_job()
        self.assertTrue(isinstance(j, Job))
        self.assertEqual(j.__str__(), f'Name: {j.name.title()}, Location: {j.location}')
        self.assertEqual(j.name, 'lake view house')

    
class TimeEntryTest(TestCase):
    pass