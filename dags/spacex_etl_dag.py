from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

with DAG(
    'spacex_etl',
    start_date=datetime(2026, 2, 6),
    schedule_interval='@daily',
    catchup=False
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

    # Определяем порядок выполнения задач
    t1 >> t2 >> t3
