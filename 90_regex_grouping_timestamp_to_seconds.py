import re
from datetime import timedelta

def convert_timestamp_into_seconds(text):
    x = re.search(r'PT(\d*H)?(\d*M)?(\d*S)', text)
    hours, minutes, seconds = 0,0,0

    if x.group(1):
        hours = int(x.group(1)[:-1])

    if x.group(2):
        minutes = int(x.group(2)[:-1])

    if x.group(3):
        seconds = int(x.group(3)[:-1])

    dt = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return dt.total_seconds()

print(convert_timestamp_into_seconds('PT34H15M30S'))
