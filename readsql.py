import configparser
from airflow.models import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator 
from airflow.operators.empty import EmptyOperator 
from jinja2 import Template

default_args = {
    'owner':'airflow',
    'retries' : 3,
    'start_date':datetime(2024,9,9),
    'retry_delay' : timedelta(minutes=2),
    'schedule_interval' : None
    }

def readConfig(**kwargs):
    ti = kwargs['ti']
    config = configparser.ConfigParser()
    config.read("/home/prkumarsharma/airflow/configs/readsql.config")
    db_name = config.get('SQLCONFIG','db_name')
    tbl_name = config.get('SQLCONFIG','table_name')
    ti.xcom_push(key='db_name',value=db_name)
    ti.xcom_push(key='tbl_name',value=tbl_name)   
    
def renderSQL(**kwargs):
    ti = kwargs['ti']
    sql_template_file='/home/prkumarsharma/airflow/dags/sqls/testdb.sql'
    db_name = ti.xcom_pull(task_ids='Read_Config',key='db_name') 
    tbl_name = ti.xcom_pull(task_ids='Read_Config',key='tbl_name')
    
    with open(sql_template_file,'r') as template_file:
        template_content=template_file.read()
    
    template=Template(template_content)
    rendered_sql=template.render(db_name=db_name,tbl_name=tbl_name)
    print("Render SQL ",rendered_sql)
    

with DAG(
    'ReadSQL',
    dag_display_name='Read SQL Using Jinja Template',
    description='An example DAG with default args and jinja template and config file read.',
    default_args=default_args,
    tags=['example']
    ) as dag:
    
    start = EmptyOperator(task_id="START",dag=dag)
    
    read_config = PythonOperator(
        task_id = "Read_Config",
        python_callable=readConfig,
        provide_context=True,
        dag=dag
    )
    
    render_sql = PythonOperator(
        task_id = 'Render_Sql',
        python_callable=renderSQL,
        provide_context=True,
        dag=dag
    )
    
    end = EmptyOperator(task_id='END',dag=dag)
    
    start >> read_config >> render_sql >> end


    
    

