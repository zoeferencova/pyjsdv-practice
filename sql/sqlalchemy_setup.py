from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

# connect to database on localhost
# echo outputs SQL instructions generated by SQLAlchemy
engine = create_engine('sqlite:///../data/nobel_winners.db', echo=True)

# base used to create table classes which will be made into db table schema's
Base = declarative_base()


# define table for winner, subclassing Base
# use SQLAlchemy's datatypes to define schema
class Winner(Base):
    # names table, will be used to retrieve it
    __tablename__ = 'winners'
    id = Column(Integer, primary_key=True)
    category = Column(String)
    name = Column(String)
    nationality = Column(String)
    year = Column(Integer)
    gender = Column(Enum('male', 'female'))

    # optional custom method, used when printing table row
    def __repr__(self):
        return f"<Winner(name={self.name}, category={self.category}, year={self.year})>"


# create engine with defined schema
Base.metadata.create_all(engine)


# adding instances with a session
Session = sessionmaker(bind=engine)
session = Session()

# ** operator unpacks first item into key-value pairs
albert = Winner(**nobel_winners[0])
session.add(albert)

# prints the set of items that have been added this session
print(session.new)

# removes instance from session
session.expunge(albert)
# removes all new objects added in session
session.expunge_all()


# note: all database insertions and deletions take place in python.
# it’s only when we use the commit method that the database is altered.
# it is best to use as little commits as possible, since this process is often slow


# adding all items from nobel_winners to session
winner_rows = [Winner(**w) for w in nobel_winners]
# add multiple rows at once
session.add_all(winner_rows)

# commit changes to database
session.commit()

# query database: get row count
print(session.query(Winner).count())

# get all Swiss winners
result = session.query(Winner).filter_by(nationality='Swiss')
print(list(result))

# get all non-Swiss physics winners
result = session.query(Winner).filter(
    Winner.category == 'Physics',
    Winner.nationality != 'Swiss')
print(list(result))

# get row by ID number
print(session.query(Winner).get(3))

# get items ordered by year
res = session.query(Winner).order_by('year')
print(list(res))


# converts sqlalchemy instance to dict
def inst_to_dict(inst, delete_id=True):
    dat = {}
    # access instance's table class to get list of column objects
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    # if delete_id is true, remove SQL primary id field
    if delete_id:
        dat.pop('id')
    return dat


# apply inst_to_dict function
winner_rows = session.query(Winner)
nobel_winners = [inst_to_dict(w) for w in winner_rows]
print(nobel_winners)


# update database row
marie = session.query(Winner).get(3)
marie.nationality = 'French'

# print changed instances not yet committed
print(session.dirty)


# delete results of a query
session.query(Winner).filter_by(name='Albert Einstein').delete()


# drop whole table
Winner.__table__.drop(engine)
