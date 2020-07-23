from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

from utils import  write_questions_to_s3, render_template

from utils import insert_question_to_db

default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2020, 7, 22),
    "email": ["ogunyemijeremiah@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
    "schedule_interval": "@daily",
}

with DAG("get_top_airflow_questions_from_stackoverflow", default_args=default_args) as dag:

    Task_I = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres_default",
        database="d83j4tcl2b575t",
        sql="""
        DROP TABLE IF EXISTS public.questions;
        CREATE TABLE public.questions
        (
            title text,
            is_answered boolean,
            link character varying,
            score integer,
            tags text[],
            question_id integer NOT NULL,
            owner_reputation integer
        )
        """,
    )

    Task_II = PythonOperator(
        task_id="insert_question_to_db", python_callable=insert_question_to_db
    )

    Task_III = PythonOperator(
        task_id="write_questions_to_s3", python_callable=write_questions_to_s3
    )

    Task_IV = PythonOperator(
        task_id="render_template",
        python_callable=render_template,
        provide_context=True,
    )

    Task_V = EmailOperator(
        task_id="send_email",
        provide_context=True,
        to="ogunyemijeremiah@gmail.com",
        subject="Top questions with tag 'airflow' on {{ ds }}",
        html_content="{{ task_instance.xcom_pull(task_ids='render_template', key='html_content') }}",
    )

Task_I >> Task_II >> Task_III >> Task_IV >> Task_V
