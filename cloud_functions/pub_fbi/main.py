import json
import urllib3
import logging
from datetime import date, timedelta
import base64
from google.cloud import storage
from google.api_core import retry
from google.cloud import bigquery

from google.cloud import pubsub_v1


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
base_url = 'https://api.usa.gov/crime/fbi/sapi/api/agencies/list'

#ori='HI0010000'
#start_date='2018'
#end_date='2019'

#*** commenting the base url to use the arguments
#print(fbi_url)

#base_url=fbi_url(base_url,ori,start_date,end_date)
#print(base_url)


#### ORI

#######

# Currently being hardcoded to Chicago but will be turned into a list of cities 
# with their latitutde  and longitude

#lat='41.8781 C2 B0 20N'
#lon='87.6298%C2%B0%20W'

#distance = '10mi'

# Get the data


# Getting the request arguments for city, distance , start date and end date

BQ_PROJECT = "msds-498-group-project"
BQ_DATASET = 'crime_data'
BQ_TABLE = 'ORI'
#topic_name = 'projects/msds-498-group-project/topics/crime_daily_data'
topic_name = 'crime_daily_data'
BQ = bigquery.Client(project=BQ_PROJECT, location='US')

table_ref = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
table = BQ.get_table(table_ref)
#print(table)

def load_into_bq(json_data):
#    print('i am inside the load function')
#    logging.Logger('i am inside load function')
    row = json_data
#    print(f'the type of the data is {type(row)}')
#    print(f'the data is \n {row}')

    row_json = row.decode('utf-8')

    row = json.loads(row_json)

    #print(f'my type before loads is {type(row)}')
    #row = row.data.decode('utf-8')
    #row = json.dumps(row)
#   print(f'the row_json  is \n {row}')
    #row = json.loads(row.data))


#    print('i am the row\n')
#    print(type(row))
#    print(f'the length of the row is : {len(row)}')
#    print(f'the first element of the row is " {row[0]}')


    row = [x for x in row if (x['county_name'] == 'COOK' and x['state_abbr'] == 'IL') or
           (x['county_name'] == 'LOS ANGELES' and x['state_abbr'] == 'CA') or
           (x['state_abbr'] == 'DC') or
           (x['county_name'] == 'KING' and x['state_abbr'] == 'WA') or
           (x['county_name'] == 'PHILADELPHIA' and x['state_abbr'] == 'PA') or
           (x['county_name'] == 'FULTON' and x['state_abbr'] == 'GA') or
           (x['county_name'] == 'DALLAS' and x['state_abbr'] == 'TX') or
           (x['county_name'] == 'HARRIS' and x['state_abbr'] == 'TX') or
           x['county_name'] == 'MIAMI-DADE' or
           x['ori'] == 'NY0303000' or
           x['ori'] == 'AZ0072300' or
           x['ori'] == 'WASPD0000' or
           x['ori'] == 'WA0173200' or
           x['ori'] == 'GAAPD0000']

    for item in row:
        if (item['county_name'] == 'COOK' and item['state_abbr'] == 'IL'):
            item.update({'city':'chicago'})
        elif (item['county_name'] == 'LOS ANGELES' and item['state_abbr'] == 'CA'):
            item.update({'city':'losangeles'})
        elif (item['state_abbr'] == 'DC'):
            item.update({'city':'washintgondc'})
        elif (item['county_name'] == 'KING' and item['state_abbr'] == 'WA'):
            item.update({'city':'seattle'})
        elif (item['county_name'] == 'PHILADELPHIA' and item['state_abbr'] == 'PA'):
            item.update({'city':'philadelphia'})
        elif (item['county_name'] == 'FULTON' and item['state_abbr'] == 'GA'):
            item.update({'city':'atlanta'})
        elif (item['county_name'] == 'DALLAS' and item['state_abbr'] == 'TX'):
            item.update({'city':'dallas'})
        elif (item['county_name'] == 'HARRIS' and item['state_abbr'] == 'TX'):
            item.update({'city':'houston'})
        elif item['county_name'] == 'MIAMI-DADE':
            item.update({'city':'miami'})
        elif item['ori'] == 'NY0303000':
            item.update({'city':'newyork'})
        elif item['ori'] == 'AZ0072300':
            item.update({'city':'phoenix'})
        elif item['ori'] == 'WASPD0000':
            item.update({'city':'seattle'})
        elif item['ori'] == 'WA0173200':
            item.update({'city':'seattle'})
        elif item['ori'] == 'GAAPD0000':
            item.update({'city':'atlanta'})
        else:
            item.update({'city':''})

    ori_list = [x['ori'] for x in row]

    # Setting for PublisherClient
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(BQ_PROJECT, topic_name)

    for ori_item in ori_list:
        message_json = json.dumps({
            'data': {'message': ori_item},
        })
        #print(f'Data is {message_json}')
        message_bytes = message_json.encode('utf-8')
        
        # Publishes a message
        try:
            publish_future = publisher.publish(topic_path, data=message_bytes)
            publish_future.result()  # Verify the publish succeeded
            #return 'Message published.'
        except Exception as e:
            print(e)
            return (e, 500)

    #print(f'the type of row after list comp is : {type(row)}')
    #print(row[0])

    #print(row['coumty_name'])
    #row_json = json.loads(row)

    #print(row_json)
    #logging.Logger([row])

    #print(f'the length of the row is : {len(row)}')
    errors = BQ.insert_rows(table, row, retry=retry.Retry(deadline=30))
    #print('The errors')
    #print(errors)
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

