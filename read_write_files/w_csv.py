import csv

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


# create new file, indicate we will be writing to it using 'w'
with open('../data/nobel_winners.csv', 'w', encoding="utf-8") as f:
    # get column headers from dict keys and sort alphabetically
    fieldnames = nobel_winners[0].keys()
    fieldnames = sorted(fieldnames)
    # use csv's DictWriter to create CSV out of dictionary, supplying header titles
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # write header
    writer.writeheader()
    # write rows
    for w in nobel_winners:
        writer.writerow(w)

# open csv file
with open('../data/nobel_winners.csv', encoding="utf-8") as f:
    # initialize reader
    reader = csv.reader(f)
    # print each row to display in readable format
    for row in reader:
        print(row)

# open csv file as a dictionary of rows
with open('../data/nobel_winners.csv', encoding="utf-8") as f:
    # create list of dictionaries (preferred)
    reader = csv.DictReader(f)
    nobel_winners = list(reader)
    for w in nobel_winners:
        w['year'] = int(w['year'])

print(nobel_winners)

# next step: pass csv-derived dict to json module
