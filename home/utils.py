from datetime import datetime
from .models import DailyOperationsHours
def get_today_operating_hours():
    today=datetime.today().strftime("%A")
    try:
        hours=DailyOperationsHours.objects.get(day=today)
        return hours.open_time,hours.close_time
    expcet DailyOperationsHours.DoesNotExist:
        return None, None