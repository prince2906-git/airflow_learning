from airflow.models import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

with DAG(
    'FirstDAG',
    description='A simple tutorial DAG',
    start_date=datetime(2024,1,1),
    tags=['example'],
) as dag:
    start = EmptyOperator(
        task_id="start"
    )
    
    transform = dummy_task = BashOperator(
        task_id="transform",
        bash_command="ls -l /home/prkumarsharma/airflow"
    )
    
    end = EmptyOperator(
        task_id="end"
    )
    
    start >> transform >> end