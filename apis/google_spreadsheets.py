import gspread
import pandas as pd

gc = gspread.service_account(
    filename='../data/pyjsviz-373207-79ed803b5cb7.json')
ss = gc.open_key=('secret')

# open specific worksheet
ws = ss.worksheet('bugs')

# print values in first column
print(ws.col_values(1))

# initialize pandas dataframe with all data
df = pd.DataFrame(ws.get_all_records(expected_headers=[]))
print(df.info())
