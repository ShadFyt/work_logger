import json
from datetime import datetime, timedelta

from ..models import TimeSheet, Job

data = []


def make_data(mock_data):
    if len(data) == 0:
        for d in range(200):
            data.append(mock_data[d])


def create_time_sheet_entries(data):
    job = Job(job_name="Big House", job_type="Sanding")
    job.save()
    start_date = datetime(2021, 1, 3)
    time_sheet_db = TimeSheet.objects.all()
    if not time_sheet_db:
        for d in range(50):
            start_date += timedelta(days=1)
            entry = TimeSheet(
                day_in_week=data[d]["day"],
                date=start_date,
                start_time=data[d]["start_time"],
                end_time=data[d]["end_time"],
                location=data[d]["location"],
                job=job,
            )
            entry.save()


def clear_data(data):
    data.clear()


def run():
    clear_data(data)
    with open("work_tracker/MOCK_DATA.json") as f:
        mock_data = json.load(f)
    make_data(mock_data)
    create_time_sheet_entries(data)
