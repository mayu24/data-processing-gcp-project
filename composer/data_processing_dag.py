from airflow import DAG
from airflow.providers.google.operators.dataproc import DataprocCreateClusterOperator, DataprocSubmitJobOperator, DataprocDeleteClusterOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dataproc_processing_dag',
    default_args=default_args,
    description='Dataproc Processing DAG',
    schedule_interval=None,  # Set to None or a specific schedule interval
)

create_cluster_task = DataprocCreateClusterOperator(
    task_id='create_dataproc_cluster',
    project_id='root-rock-413418',
    region='us-central1',
    cluster_name='my_dataproc_cluster',
    num_workers=2,
    dag=dag
)

submit_dataproc_job_task = DataprocSubmitJobOperator(
    task_id='submit_dataproc_job',
    job_name='dataproc_job',
    cluster_name='my_dataproc_cluster',
    region='your_region',
    job={
        'reference': {'projectId': 'your_project_id'},
        'placement': {'clusterName': 'my_dataproc_cluster'},
        'pysparkJob': {
            'mainPythonFileUri': 'gs://my_bucket_dataproc/my_script.py',
        },
    },
    dag=dag
)

delete_cluster_task = DataprocDeleteClusterOperator(
    task_id='delete_dataproc_cluster',
    project_id='root-rock-413418',
    region='us-central1',
    cluster_name='my_dataproc_cluster',
    trigger_rule='all_success',  # This task runs only if the previous tasks are successful
    dag=dag
)

create_cluster_task >> submit_dataproc_job_task >> delete_cluster_task
