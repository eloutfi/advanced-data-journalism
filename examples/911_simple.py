import urllib2
from bs4 import BeautifulSoup

# Define the URL we want to scrape
url = "http://cohweb.houstontx.gov/ActiveIncidents/Combined.aspx"

# Get its HTML
html = urllib2.urlopen(url).read()

# Turn the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Use the find method of the BeautifulSoup object to get the item we want
table = soup.find('table', {'id': 'GridView2'})

# Loop over all the rows in the table
for tr in table.find_all('tr'):

    # Loop over all the cells in each row
    for td in tr.find_all('td'):

        # Print the text of each cell
        print td.text