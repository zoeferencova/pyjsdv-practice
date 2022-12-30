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
f = open('data/nobel_winners.csv', 'w', encoding="utf-8")

# set columns based on dict keys and sort alphabetically
cols = nobel_winners[0].keys()
cols = sorted(cols)

# write to file
with open('data/nobel_winners.csv', 'w', encoding="utf-8") as f:
    # write column names separated by comma, followed by new line
    f.write(','.join(cols) + '\n')
    # for each item in list, create a list for the row
    for o in nobel_winners:
        # add string version of each value into list
        row = [str(o[col]) for col in cols]
        # join items in list with comma and add new line
        f.write(','.join(row) + '\n')

# print each line in csv to check output
with open('data/nobel_winners.csv', encoding="utf-8") as f:
    for line in f.readlines():
        print(line)
