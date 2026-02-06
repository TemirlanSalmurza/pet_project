# SpaceX  ETL Project

Учебный проект для практики Data Engineering с использованием Airflow, Python и PostgreSQL.

## Описание
Проект выполняет ETL (Extract, Transform, Load) данные о запусках SpaceX:
1. **Extract** — загрузка данных из API SpaceX.
2. **Transform** — подготовка и очистка данных.
3. **Load** — сохранение данных в PostgreSQL.

## Стек технологий
- Python 3.8+
- Apache Airflow 2.7
- PostgreSQL
- Docker + Docker Compose

## Запуск проекта
1. Склонировать репозиторий
2. Поднять контейнеры:
   ```bash
   docker-compose up -d pet_project
