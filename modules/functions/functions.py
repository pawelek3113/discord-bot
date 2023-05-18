import pytz
from datetime import datetime


def utc_to_local(time):
    local_tz = pytz.timezone("Europe/Warsaw")
    local_dt = time.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_dt


def format_time(time: datetime):
    new_time = time.strftime("%H:%M:%S %Z")
    return new_time
