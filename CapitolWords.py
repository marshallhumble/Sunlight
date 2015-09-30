#!/usr/bin/env python

"""
CapitolWords.py:
Pull a phrase from the Capitol Words API and place the dates of US Congress in Session,
the total count that day of the word being said, and also the tf-idf count.
The td-idf count is erm frequency–inverse document frequency which shows the word usage
in relation to other words used that day.
"""

__author__      = "Marshall Humble"
__copyright__   = "MIT License"


import requests
import json
import csv

#Define the Phrase we want to look for
my_phrase = 'economy'


def get_words(search_phrase):

    #Communitcate with the API via requests
    api_key = '<YOUR_API_KEY:https://sunlightfoundation.com/api/>'
    base_url = 'http://capitolwords.org/api/1/dates.json?'
    time_series__payload = {
        'phrase': search_phrase,
        'percentages': 'true',
        'granularity': 'day',
        'apikey': api_key
    }

    #take the response and turn it into workable JSON
    r = requests.get(base_url, params=time_series__payload)
    json_string = r.text
    new_file = my_phrase + '.csv'
    f = csv.writer(open(new_file, "wt"))
    json_data = json.loads(json_string)
    results = json_data['results']

    #write the data to a csv
    f.writerow(["date", "count", "tf-idf"])
    for x in results:
        f.writerow([x["day"],
                    x["total"],
                    x["percentage"]])


get_words(my_phrase)
