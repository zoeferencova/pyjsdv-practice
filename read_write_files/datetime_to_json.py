import datetime
import json


# subclass a JSONEncoder to create custom date-handling one
class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        # tests for datetime obj and returns isoformat if true
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def dumps(obj):
    # set custom date encoder using cls argument
    return json.dumps(obj, cls=JSONDateTimeEncoder)


# testing encoder
now_str = dumps({'time': datetime.datetime.now()})
print(now_str)
