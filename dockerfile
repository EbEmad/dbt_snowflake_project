FROM apache/airflow:2.5.1

COPY requirements.txt /requirements.txt
# Install Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the DAGs directory to the Airflow home directory
COPY dags/ /opt/airflow/dags/

# Copy the entrypoint script
COPY run.sh /run.sh

# Switch to the root user to change permissions
USER root
RUN chmod +x /run.sh
RUN apt-get update && apt-get install -y git iputils-ping


# Switch back to the airflow user
USER airflow
ENV DBT_PROFILES_DIR=/opt/airflow/snowflake_data_project/profiles


# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/run.sh"]