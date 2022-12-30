from pymongo import MongoClient


nobel_winners = [
    {'category': 'Physics',
     'name': 'Albert Einstein',
     'nationality': 'Swiss',
     'gender': 'male',
     'year': 1921},
    {'category': 'Physics',
     'name': 'Paul Dirac',
     'nationality': 'British',
     'gender': 'male',
     'year': 1933},
    {'category': 'Chemistry',
     'name': 'Marie Curie',
     'nationality': 'Polish',
     'gender': 'female',
     'year': 1911}
]


# set constant strings to avoid spelling errors and unwanted creation
DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'


# access a mongodb database
def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    ''' Get named database from MongoDB with/without authentication '''
    # make Mongo connection with/without authentication
    if username and password:
        mongo_uri = f'mongodb://{username}:{password}@{host}/{db_name}'
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db_name]


# creates or accesses nobel_prize database
db = get_mongo_database(DB_NOBEL_PRIZE)
# creates or retrieves winners collection
coll = db[COLL_WINNERS]

# insert multiple rows at once
# coll.insert_many(nobel_winners)

# get winners with category Chemistry
res = coll.find({'category': 'Chemistry'})
print(list(res))

# get winners after 1930
res = coll.find({'year': {'$gt': 1930}})
print(list(res))

# get winners after 1930 or all female winners
res = coll.find({'$or': [{'year': {'$gt': 1930}}, {'gender': 'female'}]})
print(list(res))


# turn mongodb collection into Python list of dictionaries
# empty query dict {} finds all documents in collection
# del_id removes MongoDB's ObjectId from items by default
def mongo_coll_to_dicts(dbname='test', collname='test', query={}, del_id=True, **kw):
    database = get_mongo_database(dbname, **kw)
    response = list(database[collname].find(query))

    if del_id:
        for row in response:
            row.pop('_id')

    return res


# print list of dictionaries
print(mongo_coll_to_dicts(DB_NOBEL_PRIZE, COLL_WINNERS))
