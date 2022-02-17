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
    'retry_delay': timedelta(minutes=2)
}

#######################
## 3. Instantiate a DAG
#######################

dag = DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='This is the first dag',
    start_date=datetime(2022, 2, 7),
    schedule_interval='@daily',
)

#######################
## 4. Tasks
#######################

t1 = BashOperator(
    task_id='first_task',
    bash_command='echo hello world, this is the first task!',
    dag=dag,
)

t2 = BashOperator(
    task_id='second_task',
    bash_command='echo hey I am task 2 and will be running after task 1!',
    dag=dag,
)

t3 = BashOperator(
    task_id='third_task',
    bash_command='echo hey I am task 3 and will be running after task 1 too!',
    dag=dag,
)

#######################
## 5. Setting up dependencies
#######################

t1 >> [t2, t3]
