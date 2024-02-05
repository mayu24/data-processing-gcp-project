# File: composer/my_workflow.py
from airflow import DAG
from airflow.operators import BashOperator
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
    'my_data_processing_workflow',
    default_args=default_args,
    description='A simple data processing workflow',
    schedule_interval=timedelta(days=1),
)

task_process_data = BashOperator(
    task_id='process_data',
    bash_command='python /path/to/your_script.py',
    dag=dag,
)

task_process_data

