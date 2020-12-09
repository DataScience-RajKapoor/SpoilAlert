import json
from google.cloud import bigquery
import json
import logging
import os
import traceback
from datetime import datetime

from google.api_core import retry
from google.cloud import bigquery
import pytz

BQ_PROJECT = "msds-498-group-project"
BQ_DATASET = 'crime_data'
BQ_TABLE = 'Crime_Data_Table'

BQ = bigquery.Client(project=BQ_PROJECT, location='US')


row={
      'ori':'ILCPD0000',
      'data_year': 2019,
      'offense': 'rape-legacy',
      'state_abbr': 'IL',
      'cleared': 0,
      'actual': 0
    }


#row = '\n'.join(
#   json.dumps(item)
 #   for item in row)  

    #row = json.loads(blob.download_as_string())
table = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
errors = BQ.insert_rows_json(table,
                             json_rows=[row], 
                             retry=retry.Retry(deadline=30))

