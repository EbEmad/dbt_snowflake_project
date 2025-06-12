from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

from dbt_airflow.core.config import DbtAirflowConfig, DbtProjectConfig, DbtProfileConfig
from dbt_airflow.core.task_group import DbtTaskGroup
from dbt_airflow.core.task import ExtraTask
from dbt_airflow.operators.execution import ExecutionOperator


with DAG(
    dag_id='test_dag',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': timedelta(minutes=2),
    },
) as dag:
   
    tg = DbtTaskGroup(
        group_id='dbt-company',
        dbt_project_config=DbtProjectConfig(
            project_path=Path('/opt/airflow/snowflake_data_project/'),
            manifest_path=Path('/opt/airflow/snowflake_data_project/target/manifest.json'),
        ),
        dbt_profile_config=DbtProfileConfig(
            profiles_path=Path('/opt/airflow/snowflake_data_project/profiles'),
            target='dev',
        )
    )

    tg 