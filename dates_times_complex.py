from datetime import datetime
from dateutil.parser import parse

d = datetime.now()

# this string can then be saved to JSON or CSV
# read by JS, and used to create a Date object
iso_date = d.isoformat()
print(iso_date)

# convert back to python datetime
print(parse('2022-12-30T14:11:38.317251'))
