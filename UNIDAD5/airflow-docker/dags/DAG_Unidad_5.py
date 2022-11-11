# docker stop 9c9871e0201a && docker start 9c9871e0201a
# import the libraries
import logging
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
import pandas as pd
import openpyxl


# defining DAG arguments

default_args = {
    'owner': 'Alkemy_Prisma',
    'start_date': days_ago(0),
    'email': ['some@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'DAG_Unidad_5',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)

# Tasks


@dag.task(task_id = "read_top10")
def read_top10():
    # ----- Completar logging ------

    logger = logging.getLogger("airflow.task")

    logger = logging.getLogger("custom_logger")
    level = logging.getLevelName('INFO')
    logger.setLevel(level)
    # Format
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(levelno)s - %(message)s')

    # Handler 1 - Stream Handler (INFO)
    # stream_handler = logging.StreamHandler()
    # stream_handler.setLevel(logging.INFO)
    # stream_handler.setFormatter(format)
    # logger.addHandler(stream_handler)

    # Handler 2 - File Handler (FILE)
    file_handler = logging.FileHandler('./custom_log.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)
    logger.info("Running 'read_top10'")
    
    # -----Fin Completar logging ------




    # Read CSV from web
    url = "http://winterolympicsmedals.com/medals.csv"
    
    try:
        logger.info('Reading CSV...')
        df = pd.read_csv(url)
        
        # Get top 10 countries with most medals
        top_countries = df.NOC.value_counts().sort_values(ascending=False).head(10)
        
        # Convert pandas series to data frame
        to_countries_df = top_countries.to_frame()

        # Save data frame in Excel format - Completar tu propia ubicación para guardar el archivo de salida
        to_countries_df.to_excel('./top10_medals_by_country.xlsx')

        #Logging message INFO Success --- Completar
        logger.info('...Archivo procesado correctamente...')
    except Exception as e:
        #Logging message ERROR Fail --- Completar
        logger.critical('Error al cargar o guardar archivo: ', e)

# task pipeline
read_top10()