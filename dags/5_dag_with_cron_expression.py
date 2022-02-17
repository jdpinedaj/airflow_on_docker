#######################
## 1. Importing modules
#######################

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

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
    dag_id='dag_with_cron_expression_v03',
    default_args=default_args,
    start_date=datetime(2021, 1, 1),
    schedule_interval='23 0-20/2 * * *',
)

#######################
## 4. Tasks
#######################

t1 = BashOperator(
    task_id='first_task',
    bash_command='echo dag with cron expression!',
    dag=dag,
)

#######################
## 5. Setting up dependencies
#######################

# t1 >> [t2, t3]
