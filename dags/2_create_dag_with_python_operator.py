#######################
## 1. Importing modules
#######################

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

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


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(
        f'Hello world! My name is {first_name} {last_name} and I am {age} years old!'
    )


def get_name(ti):
    ti.xcom_push(key='first_name', value='Juan')
    ti.xcom_push(key='last_name', value='Pineda')


def get_age(ti):
    ti.xcom_push(key='age', value=33)


# def greet(name, age):
#     print(f'Hello world! My name is {name} and I am {age} years old!')

# def get_name():
#     return 'Juan'

dag = DAG(
    dag_id='our_dag_with_python_operators_v05',
    default_args=default_args,
    description='Our first dag using python operators',
    start_date=datetime(2022, 2, 7),
    schedule_interval='@daily',
)

#######################
## 4. Tasks
#######################

t1 = PythonOperator(
    task_id='greet',
    python_callable=greet,
    # op_kwargs = {'name': 'Juan', 'age': 33},
    dag=dag,
)

t2 = PythonOperator(task_id='get_name', python_callable=get_name, dag=dag)

t3 = PythonOperator(task_id='get_age', python_callable=get_age, dag=dag)

#######################
## 5. Setting up dependencies
#######################

[t2, t3] >> t1
