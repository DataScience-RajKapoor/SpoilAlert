import json
from datetime import date, timedelta
import urllib3
import os
import json
import base64
from google.cloud import storage
import flask
import traceback
from google.api_core import retry
from google.cloud import bigquery
import pytz
import urllib3
import logging
#from google.cloud import pubsub_v1


# Get the data from Crimeometer API
# Generate the url for pushing to the API

#parse the content of the secret.json file
yesterday = date.today() - timedelta(1)
yesterday = str(yesterday)[:10]

storage_client = storage.Client()

# Smart way to replace json elements causing issues
# example the output was false while it should have been a string or False

false = False
null = ""
true = True

# Make choices for the tables based on the arguments
row = '[{"ori": "AK0010100","agency_name": "Anchorage Police Department","agency_type_name": "City","state_name": "Alaska","state_abbr": "AK","division_name": "Pacific","region_name": "West","region_desc": "Region IV", "county_name": "ANCHORAGE","nibrs": "False","latitude": 61.17425,"longitude": -149.284329,    "nibrs_start_date": ""}]'

def load_credentials():
    blob = storage_client.get_bucket('secrets-bucket-json')  \
        .get_blob('secrets.json') \
        .download_as_string()

    parsed = json.loads(blob)
    api_key = parsed['api_key']

    return api_key

creds = 'xLqfjj53mdIMnUbwKsjHhAH1Z9znHcoUTARxcrhn'

#base_url = 'https://api.crimeometer.com/v1/incidents/stats'

# FBI URL
base_url='https://api.usa.gov/crime/fbi/sapi/api/agencies/list'
#ori='HI0010000'
#start_date='2018'
#end_date='2019'

print('i reached here')
print(base_url)

BQ_PROJECT = "msds-498-group-project"
BQ_DATASET = 'crime_data'
BQ_TABLE = 'ORI'
#topic_name = 'projects/msds-498-group-project/topics/crime_daily_data'
topic_name='crime_daily_data'
BQ = bigquery.Client(project=BQ_PROJECT, location='US')

table_ref = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
table = BQ.get_table(table_ref)
print(table)

def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v


#row = '{"ori":"ILCPD0000","data_year":2018,"offense":"rape-legacy","state_abbr":"IL","cleared":0,"actual":0,"ori":"ILCPD0000","data_year":2018,"offense":"rape","state_abbr":"IL","cleared":0,"actual":1857}'
def load_into_bq(json_data):
    print('i am inside the load function')
    logging.Logger('i am inside load function')
    row = json_data
    print(f'the type of the data is {type(row)}')
    print(f'the data is \n {row}')

    row_json = row.decode('utf-8')

    row = json.loads(row_json)

    #print(f'my type before loads is {type(row)}')
    #row = row.data.decode('utf-8')
    #row = json.dumps(row)
    print(f'the row_json  is \n {row}')
    #row = json.loads(row.data))


    print('i am the row\n')
    print(type(row))
    print(f'the length of the row is : {len(row)}')
    print(f'the first element of the row is " {row[0]}')


    for item in row:
        if ('COOK' in item['county_name'] and item['state_abbr']=='IL'):
            item.update( {'city':'chicago'})
        elif ('LOS ANGELES' in item['county_name'] and item['state_abbr']=='CA'):
            item.update( {'city':'losangeles'})
        elif (item['state_abbr']=='DC'):
            item.update( {'city':'washintgondc'})
        elif ('KING' in item['county_name'] and item['state_abbr']=='WA'):
            item.update( {'city':'seattle'})
        elif ('PHILADELPHIA'  in item['county_name'] and item['state_abbr']=='PA'):
            item.update( {'city':'philadelphia'})
        elif ('FULTON'  in item['county_name'] and item['state_abbr']=='GA'):
            item.update( {'city':'atlanta'})
        elif ('DALLAS'  in item['county_name'] and item['state_abbr']=='TX'):
            item.update( {'city':'dallas'})
        elif ('HARRIS'  in item['county_name'] and item['state_abbr']=='TX'):
            item.update( {'city':'houston'})
        elif ('MIAMI-DADE'  in item['county_name']):
            item.update( {'city':'miami'})
        elif item['ori']=='NY0303000':
            item.update( {'city':'newyork'})
        elif item['ori']=='AZ0072300':
            item.update( {'city':'phoenix'})
        elif item['ori']=='WASPD0000':
            item.update( {'city':'seattle'})
        elif item['ori']=='WA0173200':
            item.update( {'city':'seattle'})
        elif item['ori']=='GAAPD0000':
            item.update( {'city':'atlanta'})
        else:
            None


    ori_list = [x['ori'] for x in row]
    crime_data_url = 'https://us-central1-msds-498-group-project.cloudfunctions.net/crime_data_fbi'


    
    print(len(row))

    #print(row['coumty_name'])
    #row_json = json.loads(row)

    #print(row_json)
    logging.Logger([row])

    print(f'the length of the row is : {len(row)}')
    errors = BQ.insert_rows(table,row,retry=retry.Retry(deadline=30))
    print('The errors')
    print(errors)
    #logging.Logger('I am the errors {errors}')
    return "ORI table loadsed"




def ori_data_fbi(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    http = urllib3.PoolManager()


    #base_url=fbi_url(request)
    logging.Logger(base_url)
    print('I am inside the main function')
    # New request url
    request_url = base_url
    logging.Logger(request_url)


    payload = http.request('GET',
                              request_url,
                              headers={
                                  'Content-Type': 'application/json',
                                  'x-api-key': creds
                              },
                              fields={
                              'API_KEY':creds
                              }
                           )

    #*** only changing it for testing ***
    #return request_url
   # print(f'the type of payload is\n {type(payload.data)}')
    print(payload.data)
    return load_into_bq(payload.data)
    #return payload.data
