from airflow import DAG
from airflow.contrib.operators.dataproc_operator import DataprocSubmitJobOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
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

create_table_task = BigQueryOperator(
    task_id='create_table',
    sql='CREATE TABLE IF NOT EXISTS your_dataset.processed_data (...)',
    use_legacy_sql=False,
    dag=dag
)

submit_dataproc_job_task = DataprocSubmitJobOperator(
    task_id='submit_dataproc_job',
    job={
        'reference': {'projectId': 'your_project_id'},
        'placement': {'clusterName': 'your_dataproc_cluster'},
        'pysparkJob': {
            'mainPythonFileUri': 'gs://your_bucket/your_script.py',
        },
    },
    project_id='your_project_id',
    region='your_region',
    cluster_name='your_dataproc_cluster',
    dag=dag
)

create_table_task >> submit_dataproc_job_task
