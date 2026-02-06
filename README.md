# SpaceX ETL Pipeline (Pet Project)

Pet project to practice Data Engineering stack:
SQL, Python, Airflow, Docker, Postgres.

## Architecture
API (SpaceX) → ETL (Python) → Postgres → Airflow orchestration

## Tech Stack
- Python
- SQL
- Apache Airflow
- Docker & Docker Compose
- PostgreSQL

## Pipeline Description
1. Extract data from SpaceX public API
2. Transform data into staging format
3. Load data into PostgreSQL
4. Orchestrate pipeline with Airflow DAG

## Project Structure
- dags/ – Airflow DAGs
- scripts/ – ETL logic (extract, transform, load)
- docker/ – Docker Compose setup
- sql/ – DDL scripts
- data/ – local data files (for development)

## Status
Work in progress 🚧
