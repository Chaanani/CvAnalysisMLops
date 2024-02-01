from airflow import DAG
import os
import sys
sys.path.append(os.path.abspath('../../'))
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from db_postgressql.getting_data import extract_table

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('extract_data_dag',
          default_args=default_args,
          schedule_interval='@daily')

extract_task = PythonOperator(task_id='extract_data_task',
                              python_callable=extract_table,
                              dag=dag)
