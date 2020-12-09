import base64
import json
import urllib3
from google.cloud import storage

STORAGE_CLIENT = storage.Client()

def load_credentials():
    blob = STORAGE_CLIENT.get_bucket('secrets-bucket-json')  \
        .get_blob('secrets.json') \
        .download_as_string()

    parsed = json.loads(blob)
    api_key = parsed['api_key']

    return api_key

# get the credentials
CREDS = load_credentials()
CRIME_DATA_URL = 'https://us-central1-msds-498-group-project.cloudfunctions.net/crime_data_fbi'

HTTP_ORI = urllib3.PoolManager()
# define the function
def fbi_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    resp = HTTP_ORI.request('GET',
                            CRIME_DATA_URL,
                            headers={
                                'Content-Type': 'application/json',
                                'x-api-key': CREDS
                            },
                            fields={
                                'API_KEY':CREDS,
                                'ori':pubsub_message,
                                'start_date':'2019',
                                'end_date':'2019',
                                'distance':'10'
                            }
                           )
    return resp.status


#creds = 'xLqfjj53mdIMnUbwKsjHhAH1Z9znHcoUTARxcrhn'

#creds = 'xLqfjj53mdIMnUbwKsjHhAH1Z9znHcoUTARxcrhn'
