from datetime import datetime

data = [
    {'id': 0, 'date': '2020/02/23 12:59:05'},
    {'id': 1, 'date': '2021/11/02 02:32:00'},
    {'id': 2, 'date': '2021/23/12 09:22:30'},
]

for d in data:
    try:
        # tries to match time string to a format string
        d['date'] = datetime.strptime(d['date'], '%Y/%m/%d %H:%M:%S')
    # handle time string that doesn't match strptime format
    except ValueError:
        print('Invalid date for ' + repr(d))

print(data)
