### This is as far as we got in class on Monday ###

import urllib2
from bs4 import BeautifulSoup

url = "https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"

html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser") 

### You guys figure out the rest! Your code goes below here ###