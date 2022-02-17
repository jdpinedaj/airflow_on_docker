#######################
## 1. Importing modules
#######################

from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import dag, task

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


@dag(dag_id='dag_with_taskflow_api_v01',
     default_args=default_args,
     description='Our first dag using python operators',
     start_date=datetime(2022, 2, 7),
     schedule_interval='@daily')
def hello_world_etl():

    #######################
    ## 4. Tasks
    #######################

    @task(multiple_outputs=True)
    def get_name():
        return {'first_name': 'Juan', 'last_name': 'Pineda'}

    @task()
    def get_age():
        return 33

    @task()
    def greet(first_name, last_name, age):
        print(
            f'Hello World! my name is {first_name} {last_name} and I am {age} years old.'
        )

    #######################
    ## 5. Setting up dependencies
    #######################

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'],
          age=age)


greet_dag = hello_world_etl()

#[t2, t3] >> t1