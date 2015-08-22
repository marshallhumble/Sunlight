import requests
import json
import csv

f = csv.writer(open("obama.csv", "wb+"))

api_key = 'API_KEY'

base_url = 'http://capitolwords.org/api/1/'

phrases = 'phrases.json'

dates_payload = {'phrase':'obama',
		'percentages':'true',
		'granularity':'day',
		'apikey':api_key}

r = requests.get(base_url+dates,params=dates_payload)


json_string = r.text

json_data = json.loads(json_string)

results = json_data['results']

row = 0

f.writerow(["date", "count"])

for x in results:
	 f.writerow([x["day"], 
              	x["total"],
			          x["percentage"]]) 

