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

def insert_data(data_list):
    
    # Establecer la conexión
    conn = pyodbc.connect(
        f'SERVER={SERVER};DATABASE={DATABASE};UID={USERDATA};PWD={PASSWORD};DRIVER={DRIVER}'
    )

    # Crear un cursor
    cursor = conn.cursor()

    # Consulta de inserción
    
    insert_query = "INSERT INTO stage.hired_employees(id,name,datetime,department_id,job_id)VALUES (?,?,?,?,?)"

    #Datos a insertar
    # id = "2"
    # name = "Bernardo Torres"
    # datetime = "2021-11-07T02:48:42Z"
    # department_id = "3"   
    # job_id = "4"

    #Ejecutar la consulta de inserción
    for data in data_list:
        cursor.execute(insert_query, (data["id"], data["name"], data["datetime"],data["department_id"],data["job_id"]))
         # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()
    
   

insert_data()
