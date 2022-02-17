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
    'retry_delay': timedelta(minutes=5)
}

#######################
## 3. Instantiate a DAG
#######################


def get_sklearn():
    import sklearn
    print(f'scikit-learn with version: {sklearn.__version__}')


def get_matplotlib():
    import matplotlib
    print(f'matplotlib with version: {matplotlib.__version__}')


dag = DAG(
    dag_id='dag_with_python_dependencies_v04',
    default_args=default_args,
    start_date=datetime(2022, 2, 1),
    schedule_interval='@daily',
)

#######################
## 4. Tasks
#######################

get_sklearn = PythonOperator(
    task_id='get_sklearn',
    python_callable=get_sklearn,
    dag=dag,
)

get_matplotlib = PythonOperator(
    task_id='get_matplotlib',
    python_callable=get_matplotlib,
    dag=dag,
)

#######################
## 5. Setting up dependencies
#######################

get_sklearn >> get_matplotlib