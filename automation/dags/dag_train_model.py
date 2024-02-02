from airflow import DAG
import sys
import os
sys.path.append(os.path.abspath('../../'))

from airflow.operators.python_operator import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime, timedelta
from src.model.traning_model import train_model

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('train_model_dag',
          default_args=default_args,
          schedule_interval='@daily')

wait_for_extract = ExternalTaskSensor(
    task_id='wait_for_extract_data',
    external_dag_id='extract_data_dag',
    external_task_id='extract_data_task',
    dag=dag,
)

train_task = PythonOperator(task_id='train_model_task',
                            python_callable=train_model,
                            dag=dag)



wait_for_extract >> train_task
