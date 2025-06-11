# Data Engineering Pipeline with dbt, Snowflake & Airflow

## 📌 Project Description

This is an **end-to-end data pipeline** that demonstrates modern data engineering practices using:

- **dbt (Data Build Tool)** for transforming raw data into analytics-ready models  
- **Snowflake** as the cloud data warehouse  
- **Apache Airflow** for workflow orchestration  
- **Docker** for containerized deployment

The pipeline ingests raw data, applies transformations, and creates structured data marts ready for analysis.

## 🌟 Key Features

- **Modular Data Transformations**: dbt models organized by business domains
- **Automated Scheduling**: Airflow DAGs to run pipelines on schedule  
- **Data Quality Checks**: Built-in dbt tests for validation  
- **Reproducible Environment**: Docker containers for all components  
- **Scalable Architecture**: Designed for cloud deployment  

## 📦 Prerequisites

Before you begin, ensure you have:

- [Docker](https://docs.docker.com/get-docker/) installed  
- [Docker Compose](https://docs.docker.com/compose/install/)  
- A Snowflake account with proper permissions  
- Python 3.8+ (for local development)  

## 🛠️ Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dbt-snowflake-airflow.git
cd dbt-snowflake-airflow