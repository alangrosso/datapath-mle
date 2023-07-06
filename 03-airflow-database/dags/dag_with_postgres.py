from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'alan_grosso',
}

with DAG(
    dag_id='dag_with_postgres_operator',
    default_args=default_args,
    start_date=datetime(2023, 7, 6),
    schedule_interval='@once',
    catchup=False,
    schedule=None
) as dag:
    
    task1 = PostgresOperator(
        task_id='create_pet_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            CREATE TABLE IF NOT EXISTS pet (
            pet_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            pet_type VARCHAR NOT NULL,
            birth_date DATE NOT NULL);
        """
    )

    task2 = PostgresOperator(
        task_id='create_owner_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            CREATE TABLE IF NOT EXISTS owner (
            pet_id SERIAL PRIMARY KEY,
            owner VARCHAR NOT NULL);
        """
    )

    task3 = PostgresOperator(
        task_id='insert_into_table_pet_1',
        postgres_conn_id='postgres_localhost',
        sql="""
            INSERT INTO pet ( name, pet_type, birth_date )  VALUES ( 'Max', 'Dog', '2020-07-05');
            INSERT INTO pet ( name, pet_type, birth_date )  VALUES ( 'Susie', 'Cat', '2022-05-01');
            INSERT INTO pet ( name, pet_type, birth_date )  VALUES ( 'Alaska', 'Dog', '2020-03-18');
        """
    )

    task4 = PostgresOperator(
        task_id='insert_into_table_owner_2',
        postgres_conn_id='postgres_localhost',
        sql="""
            INSERT INTO owner ( owner ) VALUES ( 'Lily');
            INSERT INTO owner ( owner ) VALUES ( 'Anne');
            INSERT INTO owner ( owner ) VALUES ( 'Kiara');
        """
    )

    task5 = PostgresOperator(
        task_id='inner_join',
        postgres_conn_id='postgres_localhost',
        sql="""
            SELECT A.*, B.owner 
            FROM pet A
            INNER JOIN owner B
                ON A.pet_id = B.pet_id
        """
    )

    task1 >> task2 >> [task3, task4] >> task5