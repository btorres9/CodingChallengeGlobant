from flask import Flask,jsonify,request
#from insertdata import insert_data
import json
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

app=Flask(__name__)

@app.route("/test",methods=['POST'])
def insert():
    data=request.get_json()
    data_json=jsonify(data).get_json()
    
    #Lo convierto en diccionario
    data_list = json.loads(data_json)
    columna= data_list[1]
    columna = list(columna.keys())
    columna= columna[1]

    conn = pyodbc.connect(
        f'SERVER={SERVER};DATABASE={DATABASE};UID={USERDATA};PWD={PASSWORD};DRIVER={DRIVER}'
    )

    # Crear un cursor
    cursor = conn.cursor()
    
    if columna == 'name':
    #Ejecutar la consulta de inserción
    # Consulta de inserción
        insert_query = "INSERT INTO stage.hired_employees(id,name,datetime,department_id,job_id)VALUES (?,?,?,?,?)"
        for data in data_list:
            cursor.execute(insert_query, (data["id"], data["name"], data["datetime"],data["department_id"],data["job_id"]))
    elif columna == 'department':
        insert_query = "INSERT INTO stage.departments(id,department)VALUES (?,?)"
        for data in data_list:
            cursor.execute(insert_query, (data["id"], data["department"]))
    elif columna == 'job':
        insert_query = "INSERT INTO stage.jobs(id,job)VALUES (?,?)"
        for data in data_list:
            cursor.execute(insert_query, (data["id"], data["job"]))
    else:
         print("No llegó ningun archivo.")

        
    # Confirmar la transacción    
    conn.commit()
    # Cerrar la conexión
    conn.close()
    
    print(f"Esta es la última fila de los datos: {data}")
    
    return ("Insercion Correcta")



if __name__ == "__main__": 
    app.run(debug=True)






