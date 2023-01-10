# pylint: disable=no-member
import pandas as pd

df_winners = pd.read_json('data/nobel_winners_cleaned.json')

for name, group in df_winners.groupby('country'):
    group.to_json('data/winners_by_country/' + name + '.json',
                  orient='records')
