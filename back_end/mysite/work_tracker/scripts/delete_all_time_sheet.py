from ..models import TimeSheet


def run():

    time_sheet = TimeSheet.objects.all()
    time_sheet.delete()
