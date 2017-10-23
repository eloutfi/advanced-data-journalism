import urllib2
from bs4 import BeautifulSoup


def get_image(link):
    '''
    Your job is to implement a function that, given a link, can retrieve
    an image of an offender associated with that link. For example, given
    this link component: 

    dr_info/colonejoseph.html

    The function should return this:

    https://www.tdcj.state.tx.us/death_row/dr_info/colonejoseph.jpg

    Notice that you're getting the partial link as input to the function via
    a variable called "link".
    '''

    # This appends the base URL onto the partial link you get from scraping
    # the index page.
    full_url = 'https://www.tdcj.state.tx.us/death_row/' + link

    ##### YOUR CODE GOES HERE #####

    # Ultimately you want this to return a variable that stores the URL to the image
    return full_url




# Most of this should be familiar. No need to modify anything below this, but some of the
# code might be helpful ...

url = 'https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html'

html = urllib2.urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'class': 'tdcj_table indent'})

for row in table.find_all('tr'):
    tds = row.find_all('td')

    # Here we're going to scrape something other than the text of the cell --
    # namely the "href" (link) attribute of the <a> tag that the "offender
    # information" tag on the page links to.

    # First we only want to scrape information if we find more than one <td>
    # tag in the row. If you look closely, you'll notice that the first, header
    # row is composed of <th> tags, not <td>. This conditional avoids an error
    # that occurs in that case.
    if len(tds) > 0:

        # Pay close attention to this. We're grabbing the second <td> tag in the
        # row (tds[1]). Then grabbing the <a> tag inside of that (tds[1].a) and
        # then grabbing the href attribute of that (tds[1].a['href']). You'll do
        # something similar in the code you write ...
        partial_url = tds[1].a['href']

        # Ho-hum, don't mind this. It's just here to make the exercise work ...
        if partial_url.endswith('html'):
            print get_image(partial_url)