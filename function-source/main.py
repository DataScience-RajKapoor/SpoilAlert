from __future__ import print_function
import base64
import json
import datetime
import re
import shutil
import sys
from google.cloud import storage
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load
from dateutil.parser import parse
from google.cloud import storage
import requests


STORAGE_CLIENT = storage.Client()
BLINK_BUCKET = STORAGE_CLIENT.get_bucket('secret-json')

def upload_from_url(bucket_id, filename, url):
    client = storage.Client()
    session = requests.Session()
    with session.get(url, stream=True) as response:
        bucket = client.get_bucket(bucket_id)
        blob = bucket.blob(filename)
        blob.upload_from_file(response.raw, content_type=response.headers.get('Content-Type'))

def load_credentials():
    blob = STORAGE_CLIENT.get_bucket('secret-json')  \
        .get_blob('blink.json') \
        .download_as_string()
    print(blob)
    parsed = json.loads(blob)
    try:
        user_name = parsed['username']
        password = parsed['password']
    except:
        print('i am an generic error')
    return user_name, password

def create_file_path():
	year = datetime.datetime.now().strftime("%Y")
	month = datetime.datetime.now().strftime("%m")
	file_path = f'/uploads/{year}/{month}'
	return file_path

def blink_video_schedule(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event."""
  
    FILENAME= 'blink_creds.json'

     #FILENAME = re.sub(r"\/.*\/(.*\.\w{1,4}",r'\1',FILE)
     #BLOB_UPLOAD = BLINK_BUCKET.blob(f"{create_file_path()[1:]}/{FILENAME}") #Set filename format (uploads/year/month/filename).
     #BLOB_UPLOAD.upload_from_filename(FILE)

    USER_NAME, PASSWORD = load_credentials()

    AUTH = Auth({"username": USER_NAME, "password": PASSWORD}, no_prompt=True)

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    if pubsub_message == 'RUN':
        blink = Blink()
        blink.auth = AUTH
        blink.start()
        AUTH.send_auth_key(blink, '167363')
        blink.setup_post_verify()

        #print(type(blink.save(f'{FILENAME}')))

        CREDS = json_load("blink_creds.json")

        blob_blink = BLINK_BUCKET.blob('blink_creds.json')

        blob_blink.upload_from_string(
        data=json.dumps(CREDS),
        content_type='application/json'
        )

        print('i am before the cameras')
        print(blink.cameras.items())
        try:
            for name, camera in blink.cameras.items():
                print('i am inside the camera')
                print(name)                   # Name of the camera
                print(camera.attributes)      # Print available attributes of camera
        except ValueError:
            print('there is some error')
        
        blink.download_videos(since='2018/07/04 09:34')
        return "SUCCESS"

    
     









