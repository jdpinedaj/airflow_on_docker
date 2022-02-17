#######################
## 1. Importing modules
#######################

from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

#######################
## 2. Default arguments
#######################

default_args = {
    'owner': 'jdpinedaj',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

#######################
## 3. Instantiate a DAG
#######################

dag = DAG(
    dag_id='dag_with_postgres_operator_v04',
    default_args=default_args,
    start_date=datetime(2022, 1, 7),
    schedule_interval='0 0 * * *'  # daily
)

#######################
## 4. Tasks
#######################

t1 = PostgresOperator(
    task_id='create_postgres_table',
    postgres_conn_id='postgres_localhost',
    sql='''
    CREATE table IF NOT EXISTS dag_runs(
        dt date,
        dag_id character varying,
        primary key (dt, dag_id)
    )
    ''',
    dag=dag,
)

t2 = PostgresOperator(
    task_id='insert_into_table',
    postgres_conn_id='postgres_localhost',
    sql='''
    INSERT INTO dag_runs (dt, dag_id)
    values ('{{ ds }}', '{{ dag.dag_id }}')
    ''',
    dag=dag,
)

t3 = PostgresOperator(
    task_id='delete_from_table',
    postgres_conn_id='postgres_localhost',
    sql='''
    DELETE FROM dag_runs 
    WHERE dt = '{{ ds }}' AND dag_id = '{{ dag.dag_id }}'
    ''',
    dag=dag,
)

#######################
## 5. Setting up dependencies
#######################

t1 >> t3 >> t2
