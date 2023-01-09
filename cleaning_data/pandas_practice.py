# pylint: disable=no-member
from io import StringIO
import pandas as pd
from pymongo import MongoClient
import sqlalchemy
from sqlalchemy.types import String


# pandas is made to manipulate row-columnar data tables with its core datatype, the DataFrame
# DataFrame is best thought of as a very fast, programmatic spreadsheet


# working with json files
# returns DataFrame, parsed from JSON file specified
df = pd.read_json('../data/nobel_winners.json')

# show top rows
print(df.head())

# show columns
print(df.columns)

# pandas rows have a single numeric index that can be accessed by the index property
# rows can also be DatetimeIndice's or PeriodIndice's for time-based data
# often, to aid selections, a column of the DataFrame will be set to the index using set_index

# set df's index to name column
df = df.set_index('name')
# select row by index label (name)
print(df.loc['Albert Einstein'])
# return index to original integer-based state
df.reset_index()

# select row by position
print(df.iloc[2])

# select column, returns pandas Series with all column fields with their DataFrame indices preserved
gender_col = df.gender  # or df['gender]
# returns head rows with just gender column
print(gender_col.head())

# selecting groups, e.g. all physics winners
cat_groups = df.groupby('category')
phy_group = cat_groups.get_group('Physics')
print(phy_group.head())

# selecting groups using bool mask to create new df
print(df[df.category == 'Physics'])


# creating and saving DataFrames

# creating DataFrame using python dictionary for demonstration purposes
# usually will do so from a file or database
df = pd.DataFrame({
    # specifying each column separately by default
    'name': ['Albert Einstein', 'Marie Curie',
             'William Faulkner'],
    'category': ['Physics', 'Chemistry', 'Literature']
})

# using from_dict to use record-based object arrays
df = pd.DataFrame.from_dict([
    {'name': 'Albert Einstein', 'category': 'Physics'},
    {'name': 'Marie Curie', 'category': 'Chemistry'},
    {'name': 'William Faulkner', 'category': 'Literature'}
])

# to convert between methods, pandas has many read_[format] and to_[format]
# methods available that can be used for almost any type of file format

# load data from json file
df = pd.read_json('../data/nobel_winners.json')

# there are various forms the json file can take, specified by option orient argument
# forms: split, records, index, columns, values (default is columns, best for data viz is records)
df = pd.read_json('../data/nobel_winners.json')
json = df.to_json('../data/data_cleaned.json', orient='records')

# you can also specify date_format (epoch, iso, etc.), double_precison, and default_handler
# to call if the object cannot be converted into json using panda's parser


# working with csv files
# conventional csv files will load without any parameters
df = pd.read_csv('../data/nobel_winners.csv')

# specify nonstandard csv elements if using | instead of , or other issues
DATA = "  `Albert Einstein`| Physics \n`Marie Curie`|  Chemistry"

df = pd.read_csv(StringIO(DATA), sep='|', names=[
                 'name', 'category'], skipinitialspace=True, quotechar="`")


# # working with excel files
# # pandas uses xlrd module to read excel 2003 and openpyxl to read excel 2007+ files
# # create and parse ExcelFile object to handle multiple sheets
# dfs = {}
# # load excel file
# xls = pd.ExcelFile('../data/nobel_winners.xlsx')
# # grab sheet by name and save to a dictionary
# dfs['WinnersSheet1'] = xls.parse('WinnersSheet1', na_values=['NA'])
# dfs['WinnersSheet2'] = xls.parse('WinnersSheet2',
#                                  # specify column by position to use as row label
#                                  index_col=1,
#                                  # list of additional strings to recognize as NaN
#                                  na_values=['-'],
#                                  # number of rows to skip before processing (e.g. metadata)
#                                  skiprows=3
#                                  )

# # another option is to use read_excel method which is a convenient way to load multiple spreadsheets
# # the only reason not to use read_excel is if you need different arguments for reading each excel sheet
# dfs = pd.read_excel('nobel_winners.xls',
#                     ['WinnersSheet1', 'WinnersSheet2'], index_col=None, na_values=['NA'])

# # specifying sheet by index or name using second sheetname parameter (0 by default)
# # returns first datasheet
# df = pd.read_excel('nobel_winners.xls')
# # return a named sheet
# df = pd.read_excel('nobel_winners.xls', 'WinnersSheet3')
# # first sheet and sheet named 'WinnersSheet3'
# df = pd.read_excel('nobel_winners.xls', [0, 'WinnersSheet3'])
# # all sheets loaded into a name-keyed dictionary
# dfs = pd.read_excel('nobel_winners.xls', sheetname=None)

# # select sheet columns to be parsed, setting integer value selects all columns up to it
# # setting list of integers selects specific columns
# # parse up to fifth column
# pd.read_excel('nobel_winners.xls', 'WinnersSheet1', parse_cols=4)
# # parse the second and fourth columns
# pd.read_excel('nobel_winners.xls', 'WinnersSheet1', parse_cols=[1, 3])

# # save df to the sheet of an excel file
# df.to_excel('nobel_winners.xlsx', sheet_name='WinnersSheet1')

# # select multiple df's to write to shared excel file
# with pd.ExcelWriter('nobel_winners.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='WinnersSheet1')
#     df2.to_excel(writer, sheet_name='WinnersSheet2')


# working with sql
# pandas uses SQLAlchemy for database abstraction
engine = sqlalchemy.create_engine('sqlite:///../data/nobel_winners.db')
# read_sql can read table or query depending on first argument
df = pd.read_sql('winners', engine)

# save DataFrame df to nobel_winners SQL table
df.to_sql('winners_copy', engine, if_exists='replace')

# write 500 rows at a time, avoids packet-size limiation errors
df.to_sql('winners_copy', engine, chunksize=500, if_exists='replace')

# pandas infers datatype of objects
# override default type, specify year as String column
df.to_sql('winners_copy', engine, dtype={'year': String}, if_exists='replace')


# working with mongodb
# it is useful to work with mongodb because it uses bson (binary json)
# this allows a simple connection between web-based json and backend server

# create mongo client using default host and ports
client = MongoClient()
# get nobel_prize database
db = client.nobel_prize
# find all documents in winner collection
cursor = db.winners.find()
# load all documents from cursor into a list and use to create df
df = pd.DataFrame(list(cursor))
# at this point, winners collection will be empty and ready to fill with df data


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


db = get_mongo_database('nobel_prize')
# converts df to dict in records format
records = df.to_dict('records')
# use insert for PyMongo v2, insert_many for older
# db[collection].insert(records)


# pandas doesn't have mongodb convenience methods like to_csv or read_csv
# custom utility functions
def mongo_to_dataframe(db_name, collection, query=None,
                       host='localhost', port=27017,
                       username=None, password=None,
                       no_id=True):
    """ create a DataFrame from mongodb collection """

    if not query:
        query = {}

    database = get_mongo_database(db_name, host, port, username,
                                  password)
    cursor1 = database[collection].find(query)
    dataframe = pd.DataFrame(list(cursor1))

    if no_id:
        del dataframe['_id']

    return dataframe


def dataframe_to_mongo(dataframe, db_name, collection,
                       host='localhost', port=27017,
                       username=None, password=None):
    """ save a DataFrame to mongodb collection """
    database = get_mongo_database(db_name, host, port, username,
                                  password)

    records1 = dataframe.to_dict('records')
    database[collection].insert_many(records1)


db = get_mongo_database('nobel_prize')
list(db.winners.find())


# series into dataframes
# series is like a column in a table - a one-dimensional array holding data of any type
# creating series from python list or numpy array
# automatically creates integer indices
s = pd.Series([1, 2, 3, 4])

# specify colum indices if adding row of data to df table
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# specify both data and index using python dict
# any unmatched indices will be set to NaN
# any unmatched data will be discarded
s = pd.Series({'a': 1, 'b': 2, 'c': 3})

# use scalar value to apply same value to multiple indices
# this will apply 9 to indices a, b, and c
pd.Series(9, {'a', 'b', 'c'})

# series are like numpy arrays (ndarray) so they can be passed to most numpy functions
# slicing operations also work as they would with python lists and index lables are preserved
# unlike numpy's arrays, pandas' series can take data of multiple types
# adding two series with string and number types will add the numbers and concatenate the strings

# join series together
names = pd.Series(['Albert Einstein', 'Marie Curie'], name='name')
categories = pd.Series(['Physics', 'Chemistry'], name='category')
# axis = 1 indicates that series are columns
df = pd.concat([names, categories], axis=1)
