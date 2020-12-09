import json
from google.cloud import bigquery
BQ = bigquery.Client()
BQ_DATASET = 'crime_data'

payload = { "results" : [ { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "violent-crime", "state_abbr" : "IL", "cleared" : 0, "actual" : 27420 }]}

def load_into_s3(payload):

    payload_nl = '\n'.join(
             json.dumps(item)
             for item in payload)  

    #row = json.loads(blob.download_as_string())
    table = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
    errors = BQ.insert_rows_json(table,
                                 json_rows=[row], 
                                 row_ids=[file_name],
                                 retry=retry.Retry(deadline=30))

    payload_nl = '\n'.join(
        json.dumps(item)
            for item in payload)  # Required for Newline delimited json

         # Name the file to be stored in the bucket for Big Query pul

    file_name = 'crime_data_{}'.format(yesterday.replace('-', ''))

         # Upload the file to S3
    storage_client.get_bucket(RAW_DATA).blob(file_name).upload_from_string(
             payload_nl)
    print('i am here')
    return 1

load_into_s3(payload)
