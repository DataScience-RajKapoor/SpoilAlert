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

# Get the data from Crimeometer API
# Generate the url for pushing to the API

#parse the content of the secret.json file
yesterday = date.today() - timedelta(1)
yesterday = str(yesterday)[:10]

storage_client = storage.Client()

# Make choices for the tables based on the arguments

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
base_url='https://api.usa.gov/crime/fbi/sapi/api/agencies'
#ori='HI0010000'
#start_date='2018'
#end_date='2019'

print('i reached here')
print(base_url)

#*** commenting the base url to use the arguments
#print(fbi_url)

#base_url=fbi_url(base_url,ori,start_date,end_date)
#print(base_url)


#### ORI 

#######

# Currently being hardcoded to Chicago but will be turned into a list of cities with their latitutde  and longitude

#lat='41.8781 C2 B0 20N'
#lon='87.6298%C2%B0%20W'

#distance = '10mi'

# Get the data


# Getting the request arguments for city, distance , start date and end date

BQ_PROJECT = "msds-498-group-project"
BQ_DATASET = 'crime_data'
BQ_TABLE = 'ORI'

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


def load_into_bq(json_data):
    print('i am inside the load function')
    logging.Logger('i am inside load function')
    row = json_data
    row = row.data.decode('utf-8')
    #row = json.dumps(row)
    row = json.loads(row)
    print('\ni am the row type\n')
    print(type(row))
    
    #row = [x for x in row if (row[][['county_name']=='Cook' and row['state_abbr'=='IL']) or 
    #(row['county_name']=='HARRIS' and row['state_abbr'=='TX']) or
    #(row['county_name']=='LOS ANGELES' and row['state_abbr'=='CA']) or
    #(row['state_abbr'=='DC']) or
    #(row['county_name']=='KING' and row['state_abbr'=='WA'])]
    #print(row['coumty_name'])
    #row_json = json.loads(row)

    #print(row_json)
    logging.Logger(row)
    
    print(row.keys())
    #row_HI = json.dumps(row['HI'])
    # dict to json to use insert_rows_json api
    errors = BQ.insert_rows_json(table,[row],retry=retry.Retry(deadline=30))
    #errors = BQ.insert_rows_json(table,[row['HI']],retry=retry.Retry(deadline=30))
    print('i am the error\n')
    print(errors)
    print('\nafter the error\n')
    return "BigQuery Data Complete"

def crime_data_fbi(request):
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
    return load_into_bq(payload)
    #return payload.data

#payload = crime_data_fbi(request)

#print(payload.data.decode('utf-8'))

#def load_into_s3(payload):

#     action = base64.b64decode(data['data']).decode(
#         'utf-8')  # retrieve pubsub message

#     if (action == "download!"):  # work is conditional on message content
#         payload_data = get_crime_data(payload)

#         payload_nl = '\n'.join(
#             json.dumps(item)
#             for item in payload)  # Required for Newline delimited json

#         # Name the file to be stored in the bucket for Big Query pul

#         file_name = 'crime_data_{}'.format(yesterday.replace('-', '')

#         # Upload the file to S3
#         storage_client.get_bucket(RAW_DATA).blob(file_name).upload_from_string(
#             payload_nl)
