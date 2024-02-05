# File: cloud_functions/data_ingestion.py
from google.cloud import storage, bigquery

def ingest_data(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    # Extracting bucket and file information from the event
    bucket_name = event['bucket']
    file_name = event['name']

    # Initialize Cloud Storage and BigQuery clients
    storage_client = storage.Client()
    bigquery_client = bigquery.Client()

    # Get the bucket containing the file
    bucket = storage_client.bucket(bucket_name)

    # Get the blob
    blob = bucket.blob(file_name)

    # Download the blob's contents as a bytes object
    data = blob.download_as_string()

    # Specify BigQuery details
    dataset_id = "your_dataset_id"
    table_id = "your_table_id"
    project_id = "your_project_id"

    # Construct BigQuery table reference
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)

    # Load data into BigQuery table
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON

    load_job = bigquery_client.load_table_from_json(
        data, table_ref, job_config=job_config
    )

    # Wait for the job to complete
    load_job.result()

    print(f"Data ingested into BigQuery table {project_id}.{dataset_id}.{table_id}.")

    return "Data ingestion complete."
