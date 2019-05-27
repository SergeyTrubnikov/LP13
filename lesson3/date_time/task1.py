import datetime

print("Today: {}".format(datetime.datetime.today().strftime("%d/%m/%Y")))
print("Yesterday: {}".format((datetime.datetime.today   () - datetime.timedelta(days=1)).strftime("%d/%m/%Y")))
print("Month ago: {}".format((datetime.datetime.today   () - datetime.timedelta(days=31)).strftime("%d/%m/%Y")))
