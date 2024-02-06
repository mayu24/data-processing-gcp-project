from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyTableOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_processing_dag',
    default_args=default_args,
    description='Data Processing DAG',
    schedule_interval='@daily',
)

create_table_task = BigQueryCreateEmptyTableOperator(
    task_id='create_table',
    dataset_id='your_dataset',
    table_id='processed_data',
    gcp_conn_id='google_cloud_default',
    dag=dag
)

submit_dataproc_job_task = DataprocSubmitJobOperator(
    task_id='submit_dataproc_job',
    job_name='dataproc_job',
    gcp_conn_id='google_cloud_default',
    project_id='root-rock-413418',
    cluster_name='my-dataproc-cluster',
    region='us-central1',
    job={
        'reference': {'projectId': 'root-rock-413418'},
        'placement': {'clusterName': 'my-dataproc-cluster'},
        'pysparkJob': {
            'mainPythonFileUri': 'gs://my_bucket_dataproc/my_script.py',
        },
    },
    dag=dag
)

create_table_task >> submit_dataproc_job_task
