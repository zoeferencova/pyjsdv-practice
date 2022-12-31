from bs4 import BeautifulSoup
import requests
import requests_cache

BASE_URL = 'http://en.wikipedia.org'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# create cache that will automatically cache return data from requests
# create a cache named nobel_pages, using sqlite backend, expiring after two hours
# expiration is set in order to get rid of old data
# data is updated next time there is a request for the data from a user
requests_cache.install_cache(
    'data/nobel_pages', backend='sqlite', expire_after=7200)


def get_nobel_soup():
    ''' Return a parsed tag tree of our Nobel prize page '''
    # make request to the Nobel page, setting headers
    response = requests.get(
        BASE_URL + '/wiki/List_of_Nobel_laureates',
        headers=HEADERS,
        timeout=10)

    # return the content and parse
    return BeautifulSoup(response.content, 'lxml')


# create variaible for entire page
soup = get_nobel_soup()

# find table, pass tag name and dictionary with identifiers
# this method is fragile because the order of the classes matters,
# and could be easily changed
soup.find('table', {'class': 'wikitable sortable'})

# since we specified the lxml parser, we can use the select method instead
# this method takes chained selectors and converts them to the xpath syntax internally
# select returns an array of results, select-one returns just one
soup.select('table.sortable.wikitable')
table = soup.select_one('table.sortable.wikitable')

# select table header
# can use select shorthand below, which is equivalent to table.select('th')
table('th')


def get_column_titles(winner_table):
    ''' Get the Nobel categories from the table header '''
    cols = []
    # select first row, then select all th values in array, after first
    # loop through this array and select a tag with column text and link
    for table_header in winner_table.select_one('tr').select('th')[1:]:
        link = table_header.select_one('a')
        # store category name and wikipedia link
        if link:
            cols.append({'name': link.text,
                         'href': link.attrs['href']})
        else:
            cols.append({'name': link.text, 'href': None})
    return cols


def get_nobel_winners(winner_table):
    # get column titles first
    cols = get_column_titles(winner_table)
    winners = []
    # loop through rows, skipping the first and last
    for row in winner_table.select('tr')[1:-1]:
        # get year from first cell in each row
        year = int(row.select_one('td').text)
        # loop through each cell in the row
        for i, cell in enumerate(row.select('td')[1:]):
            # for each winner value, select a tag with text and link
            for winner in cell.select('a'):
                # each winner will show up separately, and we filter out None values
                # because each has their own link and None has no link
                href = winner.attrs['href']
                # filter out cite note links
                if not href.startswith('#cite_note'):
                    winners.append({
                        'year': year,
                        'category': cols[i]['name'],
                        'name': winner.text,
                        'link': winner.attrs['href']
                    })
    return winners
