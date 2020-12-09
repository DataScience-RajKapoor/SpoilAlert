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

#row = '{"ori":"ILCPD0000","data_year":2018,"offense":"rape-legacy","state_abbr":"IL","cleared":0,"actual":0,"ori":"ILCPD0000","data_year":2018,"offense":"rape","state_abbr":"IL","cleared":0,"actual":1857}'
row = [ { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "violent-crime", "state_abbr" : "IL", "cleared" : 0, "actual" : 27420 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "rape-legacy", "state_abbr" : "IL", "cleared" : 0, "actual" : 0 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "rape", "state_abbr" : "IL", "cleared" : 0, "actual" : 1857}] 

#row = '\n'.join(
#   json.dumps(item)
#    for item in row)  

    #row = json.loads(blob.download_as_string())
table_ref = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
table = BQ.get_table(table_ref)
print(table)
errors = BQ.insert_rows(table,
                             row,
                             retry=retry.Retry(deadline=30))
print(errors)