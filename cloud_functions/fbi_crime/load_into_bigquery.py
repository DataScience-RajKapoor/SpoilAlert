import json
from google.cloud import bigquery
import json
import logging
import os
import traceback
from datetime import datetime
import traceback
from google.api_core import retry
from google.cloud import bigquery
import pytz
import urllib3

BQ_PROJECT = "msds-498-group-project"
BQ_DATASET = 'crime_data'
BQ_TABLE = 'Crime_Data_Table'

BQ = bigquery.Client(project=BQ_PROJECT, location='US')
table_ref = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
table = BQ.get_table(table_ref)
print(table)

#row = '{"ori":"ILCPD0000","data_year":2018,"offense":"rape-legacy","state_abbr":"IL","cleared":0,"actual":0,"ori":"ILCPD0000","data_year":2018,"offense":"rape","state_abbr":"IL","cleared":0,"actual":1857}'
def load_into_bq(json_data):
    print('i am inside load function')
    row = json_data
    row = row.data.decode('utf-8')
    #row = json.dumps(row)
    row = json.loads(row)
    #row_json = json.loads(row)

    #print(row_json)
    print(row['results'])
    
    
    print('here is the type')
    #print(row)
    errors = BQ.insert_rows(table,row['results'],retry=retry.Retry(deadline=30))
    return "BigQuery Data Complete"