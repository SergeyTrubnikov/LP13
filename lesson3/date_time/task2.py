import datetime

date_str = "01/01/17 12:10:03.234567"
dt_format = "%d/%m/%y %H:%M:%S.%f"
date_dt = datetime.datetime.strptime(date_str, dt_format)

print(date_dt)

