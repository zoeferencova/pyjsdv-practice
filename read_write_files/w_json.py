import json

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

with open('data/nobel_winners.json', 'w', encoding="utf-8") as f:
    # takes python container and file pointer, saves container contents to file
    json.dump(nobel_winners, f)

# open and load json file
with open('data/nobel_winners.json', encoding="utf-8") as f:
    nobel_winners = json.load(f)

print(nobel_winners)
