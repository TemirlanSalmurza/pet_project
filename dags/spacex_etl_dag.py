from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def extract_data():
    print("extracting data")

def transform_data():
    print("transforming data")

def load_data():
    print("loading data")


with DAG(
    'spacex_etl',
    
    start_date=datetime(2024, 1, 1), 
    schedule='@daily',
    catchup=False,
    
    tags=['spacex', 'etl']
) as dag:

    t1 = PythonOperator(
        task_id='extract',
        python_callable=extract_data
    )

    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform_data
    )

    t3 = PythonOperator(
        task_id='load',
        python_callable=load_data
    )

    
    t1 >> t2 >> t3
