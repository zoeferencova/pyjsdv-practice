import dataset
import datetime
from flask import Flask, request, abort
import json


app = Flask(__name__)
db = dataset.connect('sqlite:///data/nobel_winners_clean.db')


@app.route('/api/winners')
def get_country_data():
    print('Request args: ', str(dict(request.args)))
    query_dict = {}
    # restricts database queries to keys in this list
    for key in ['country', 'category', 'year']:
        # gives us access to arguments of request (written with ? and & symbols)
        arg = request.args.get(key)
        if arg:
            query_dict[key] = arg

    # dataset's find requires arg dict to be unpacked with **
    # response is then converted to a list
    winners = list(db['winners'].find(**query_dict))
    if winners:
        return dumps(winners)
    abort(404)  # resource not found


# specialized JSON encoder
class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        else:
            return json.JSONEncoder.default(self, o)


def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
