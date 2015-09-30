#!/usr/bin/env python

"""
CapitolWords.py:
Pull a phrase from the Capitol Words API and place the dates of US Congress in Session,
the total count that day of the word being said, and also the tf-idf count.
The td-idf count is erm frequency–inverse document frequency which shows the word usage
in relation to other words used that day.
"""

__author__ = "Marshall Humble"
__copyright__ = "MIT License"

import requests, json, csv
from os import path
from sys import exit

# Define the Phrase we want to look for
my_phrase = 'economy'
csv_file = my_phrase + '.csv'


def get_words(search_phrase):
    # Communitcate with the API via requests
    api_key = '<YOUR API KEY>'
    base_url = 'http://capitolwords.org/api/1/dates.json?'
    time_series__payload = {
        'phrase': search_phrase,
        'percentages': 'true',
        'granularity': 'day',
        'apikey': api_key
    }

    # Check to see if the file exists, if it does not get it.
    if path.isfile(csv_file) == False:

        #Let's try to grab the info from the API
        try:
            r = requests.get(base_url, params=time_series__payload)

        #Handle the various requests
        except requests.exceptions.Timeout:
            print("Request timeout.")
        except requests.exceptions.TooManyRedirects:
            print("Incorrect URL, please check")
        except requests.exceptions.RequestException as e:
            print (e)
            exit(1)
        else:

            #clean up the JSON
            json_string = r.text
            json_data = json.loads(json_string)
            results = json_data['results']

            # write the data to a csv
            f = csv.writer(open(csv_file, "wt"))
            f.writerow(["date", "count", "tf-idf"])
            for x in results:
                f.writerow([x["day"],
                            x["total"],
                            x["percentage"]])
            print (csv_file, "written, exiting")
            exit(0)

    #Exit if the file already exists
    elif path.isfile(csv_file)  == True:
        print (csv_file, "exists, exiting")
        exit(0)

get_words(my_phrase)
