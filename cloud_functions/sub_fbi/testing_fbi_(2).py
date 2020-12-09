import json
from datetime import date, timedelta
import urllib3
import os
import json
import base64
from google.cloud import storage 


def fbi_url(request):
    request_args = request.args
    print('request_args')
    ori=request_args['ori']
    start_date=request_args['start_date']
    end_date=request_args['end_date']
    distance=request_args['distance']
    
    return f'{base_url}/{ori}/offenses/{start_date}/{end_date}'

base_url=fbi_url(request)
print(base_url)