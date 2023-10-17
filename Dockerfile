FROM ubuntu

RUN apt update
RUN apt install python3-pip -y


# Establecemos un directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el código fuente de la aplicación al contenedor
COPY . .

# Instalamos las dependencias
RUN pip install -r requirements.txt


# Comando para iniciar la aplicación Flask
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]