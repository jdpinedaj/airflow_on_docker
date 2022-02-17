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
    dag_id='dag_with_catchup_and_backfill_v02',
    default_args=default_args,
    start_date=datetime(2022, 2, 1),
    schedule_interval='@daily',
    catchup=
    False,  # By default=True. If I turn off (False), it will run just the last day
)

#######################
## 4. Tasks
#######################

t1 = BashOperator(
    task_id='task1',
    bash_command='echo This is a simple bash command!',
    dag=dag,
)

#######################
## 5. Setting up dependencies
#######################

#
