import argparse
import datetime
import json
import time

from bs4 import BeautifulSoup
import dateparser
import requests

SCRAPER_NAME = "HOUSTON911"

def to_timestamp(time_string):
    try:
        parsed_time = dateparser.parse(time_string)
        parsed_timetuple = parsed_time.timetuple()
        timestamp = time.mktime(parsed_timetuple)
        stringified_timestamp = str(timestamp).split('.')[0]
    except:
        pass

    return None

def to_bool(possible_bool):
    if possible_bool.strip().lower() in ['true', '1', 't', 'y', 'yes']:
        return True
    if possible_bool.strip().lower() in ['false', '0', 'f', 'n', 'no']:
        return False
    return possible_bool

def scrape():
    url = "http://cohweb.houstontx.gov/ActiveIncidents/Combined.aspx"

    out_json = []

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    rows = soup.select('table#GridView2 tr')[1:]

    for row in rows:
        cells = row.select('td')
        row_dict = {}
        row_dict['agency'] = cells[0].text.strip()
        row_dict['address'] = cells[1].text.strip()
        row_dict['cross_street'] = cells[2].text.strip()
        row_dict['key_map'] = cells[3].text.strip()
        row_dict['call_time_opened_raw'] = cells[4].text.strip()
        row_dict['call_time_opened_parsed'] = to_timestamp(cells[4].text.strip())
        row_dict['incident_type'] = cells[5].text.strip()
        row_dict['combined_response'] = to_bool(cells[6].text.strip())

        print(row_dict)

        out_json.append(row_dict)

    return({"results":out_json, "last_scrape": datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})


def scrape_and_write(outfile):
    try:
        data = scrape()
    except Exception as e:
        print("{}: scraping error: {}".format(SCRAPER_NAME,e))

    if outfile:

        try:
            with open(outfile, 'w') as f:
                f.write(json.dumps(data))

        except Exception as e:
            print("{}: writing error: {}".format(SCRAPER_NAME, e))