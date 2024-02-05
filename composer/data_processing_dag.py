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
    project_id='your_project_id',
    cluster_name='your_dataproc_cluster',
    region='your_region',
    job={
        'reference': {'projectId': 'your_project_id'},
        'placement': {'clusterName': 'your_dataproc_cluster'},
        'pysparkJob': {
            'mainPythonFileUri': 'gs://your_bucket/your_script.py',
        },
    },
    dag=dag
)

create_table_task >> submit_dataproc_job_task
