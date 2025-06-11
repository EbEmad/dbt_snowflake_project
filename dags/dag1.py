from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 6, 11),  # Change as needed
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    dag_id='dbt_workflowv8',
    default_args=default_args,
    description='Run dbt models using dbt Core',
    schedule='@daily',  # Run daily
    catchup=False,
)
# Define the path to your dbt project
DBT_PROJECT_DIR = "/opt/airflow/snowflake_data_project"
DBT_PROFILES_DIR = "/opt/airflow/snowflake_data_project/profiles"  # Adjust as needed
# Task 1: Run dbt models
# Task 1: Run staging models
dbt_run_staging = BashOperator(
    task_id='dbt_run_staging',
    bash_command=f'cd {DBT_PROJECT_DIR} && dbt run --profiles-dir {DBT_PROFILES_DIR} --select staging',
    dag=dag,
)

# Task 2: Run marts models
dbt_run_marts = BashOperator(
    task_id='dbt_run_marts',
    bash_command=f'cd {DBT_PROJECT_DIR} && dbt run --profiles-dir {DBT_PROFILES_DIR} --select marts',
    dag=dag,
)

# Task 3: Run dbt tests after all models are built
dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command=f'cd {DBT_PROJECT_DIR} && dbt test --profiles-dir {DBT_PROFILES_DIR}',
    dag=dag,
)

# Define task dependencies
dbt_run_staging >> dbt_run_marts >> dbt_test
