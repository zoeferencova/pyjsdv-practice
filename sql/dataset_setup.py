import dataset

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

# connect to existing nobel_winners database
db = dataset.connect('sqlite:///../data/nobel_winners.db')

# grab table from db
wtable = db['winners']
# return all rows
winners = wtable.find()
# create list
winners = list(winners)
print(winners)


# drop table, so that we can recreate
wtable.drop()


# dataset does not require us to define schema
# create database transaction to insert objects and then commit
with db as tx:
    tx['winners'].insert_many(nobel_winners)

print(list(db['winners'].find()))
