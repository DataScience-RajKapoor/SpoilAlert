import json
from datetime import date, timedelta
import urllib3
import os
import json
import base64
from google.cloud import storage
from google.api_core import retry
from google.cloud import bigquery 
import flask
import load_into_bigquery

# Get the data from Crimeometer API
# Generate the url for pushing to the API

#parse the content of the secret.json file
yesterday = date.today() - timedelta(1)
yesterday = str(yesterday)[:10]

storage_client = storage.Client()

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
base_url='https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies'
#ori='HI0010000'
#start_date='2018'
#end_date='2019'

print('i hreached here')
print(base_url)


def fbi_url(request_url):

    request_args = request_url.args
    print('request_args')

    ori=request_args['ori']
    start_date=request_args['start_date']
    end_date=request_args['end_date']
    distance=request_args['distance']
    
    return f'{base_url}/{ori}/offenses/{start_date}/{end_date}'

#*** commenting the base url to use the arguments
#print(fbi_url)

#base_url=fbi_url(base_url,ori,start_date,end_date)
#print(base_url)


#######

# Currently being hardcoded to Chicago but will be turned into a list of cities with their latitutde  and longitude

#lat='41.8781 C2 B0 20N'
#lon='87.6298%C2%B0%20W'

#distance = '10mi'

# Get the data


    # Getting the request arguments for city, distance , start date and end date 

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

    # Getting the request arguments for city, distance , start date and end date 

    #request_args = request.args
    #print('request_args')
    #ori=request_args['ori']
    #start_date=request_args['start_date']
    #end_date=request_args['end_date']
    #distance=request_args['distance']
    base_url=fbi_url(request)
    print(base_url)
    
    # New request url 
    request_url = base_url
    print(request_url)
 
    print("i am inside the functino")
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
    #return payload
    return load_into_bigquery.load_into_bq(payload)
    
    

#payload = crime_data_fbi(http.request)

#print(payload.data.decode('utf-8'))

# def load_into_s3(payload):

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


