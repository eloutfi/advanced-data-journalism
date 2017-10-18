import urllib2, csv
from bs4 import BeautifulSoup

output_file = open('jail.csv', 'w')
writer = csv.writer(output_file)

# The site we're scraping. This is represented as a string.
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s'

# Now we're going to use a tool called urllib2 to retrieve the HTML for the site
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

inmate_table = soup.find('tbody', {'id': 'mrc_main_table'})

# Grab the rows from the table, represented as a list
row_list = inmate_table.find_all('tr')

# Loop over each of the rows
for row in row_list:

    cell_list = row.find_all('td')

    data = [cell.text.encode('utf-8').strip() for cell in cell_list]

    writer.writerow(data)