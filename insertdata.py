import pyodbc
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

#Parámetros de conexión a la base de datos de Azure
SERVER  =  os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
USERDATA = os.getenv("USERDATA")
PASSWORD = os.getenv("PASSWORD")
DRIVER =  os.getenv("DRIVER")

def insert_data():
    
    # Establecer la conexión
    conn = pyodbc.connect(
        f'SERVER={SERVER};DATABASE={DATABASE};UID={USERDATA};PWD={PASSWORD};DRIVER={DRIVER}'
    )

    # Crear un cursor
    cursor = conn.cursor()

    # Consulta de inserción
    insert_query = "INSERT INTO Stage.fact_employees(id,name,datetime,department_id,job_id)VALUES (?,?,?,?,?)"

    # Datos a insertar
    id = 4
    name = "Emanuel Anchique"
    datetime = "2021-11-07T02:48:42Z"
    department_id = 4
    job_id = 4

    # Ejecutar la consulta de inserción
    cursor.execute(insert_query, (id, name, datetime,department_id,job_id))

    # Confirmar la transacción
    conn.commit()

    # Cerrar la conexión
    conn.close()

insert_data()
