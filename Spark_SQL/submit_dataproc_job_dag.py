from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.dataproc import  DataprocCreateClusterOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocDeleteClusterOperator

default_args = {
    'depends_on_past': False   
}

CLUSTER_NAME = 'demo-airflow-cluster'
REGION='europe-west1'
PROJECT_ID='root-rock-413418'
PYSPARK_URI='gs://my_bucket_dataproc/spark_sql_script.py'


CLUSTER_CONFIG = {
    "master_config": {
        "num_instances": 1,
        "machine_type_uri": "e2-medium",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 32},
    },
    "worker_config": {
        "num_instances": 2,
        "machine_type_uri": "e2-medium",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 32},
    }
}


PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": 
       {"main_python_file_uri": PYSPARK_URI,
        'jar_file_uris': ['gs://my_bucket_dataproc/spark-3.1-bigquery-0.36.1.jar']
       }

}

with DAG(
    'Spark-Sql-Dataproc-JobWorkflow-Automation',
    default_args=default_args,
    description='A simple DAG to create a Dataproc workflow',
    schedule_interval=None,
    start_date = days_ago(2)
) as dag:

    create_cluster = DataprocCreateClusterOperator(
        task_id="Create_Dataproc_Cluster",
        project_id=PROJECT_ID,
        cluster_config=CLUSTER_CONFIG,
        region=REGION,
        cluster_name=CLUSTER_NAME,
    )

    submit_job = DataprocSubmitJobOperator(
        task_id="Spark_Sql_Task", 
        job=PYSPARK_JOB,
        region=REGION,
        project_id=PROJECT_ID, 

    )

    delete_cluster = DataprocDeleteClusterOperator(
        task_id="Delete_Dataproc_cluster", 
        project_id=PROJECT_ID, 
        cluster_name=CLUSTER_NAME, 
        region=REGION
    )

    create_cluster >> submit_job >> delete_cluster