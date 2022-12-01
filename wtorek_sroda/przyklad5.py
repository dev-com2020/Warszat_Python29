import zoneinfo
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2022, 11, 29, tzinfo=ZoneInfo("Europe/Vienna"))
print(zoneinfo.available_timezones())
print(dt)