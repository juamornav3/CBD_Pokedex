# CBD_Pokedex
Este proyecto es para aprender a manejar cursores de MongoDB utilizando una base de datos de pokémon.
# Instrucciones de instalación:
En el siguiente apartado se ofrece un pequeño manual de instalación con los pasos a seguir para utilizar el proyecto en una máquina de manera local. Dichos pasos son los siguientes:

- Paso 1: Acceder al repositorio ubicado en GitHub mediante el siguiente enlace: https://github.com/juamornav3/CBD_Pokedex/tree/juamornav3.

- Paso 2: Copiar el enlace del repositorio 

- Paso 3: Abrir entorno de desarrollo (Preferiblemente Visual Studio Code), y clonar el repositorio con el enlace copiado anteriormente:

- Paso 4: En Visual Studio Code, creamos un terminal e instalamos Python 3 (En el siguiente enlace puedes acceder a la página de descargas de Python https://www.python.org/downloads/)

- Paso 5: Dentro del terminal, ejecutar el siguiente comando para instalar todo lo necesario cómodamente (pip install -r requirements.txt).

Antes de poder arrancar la aplicación, debemos instalar MongoDB para poder conectar el proyecto a la base de datos:

- Paso 1: Accedemos a la página oficial de   MongoDB (https://www.mongodb.com/try/download/community) y descargamos la versión para Windows 10:

- Paso 2: Creamos un directorio de la siguiente manera: C:\data\db

- Paso 3: Una vez descargado el instalador, damos doble clic en el archivo para instalar MongoDB, seleccionamos el modo “Completo” y marcamos la opción para instalar el cliente Compass. De esta manera podéis ver la base de datos de una forma más sencilla.

- Paso 4: Accedemos al path: “C:\Program Files\MongoDB\Server\7.0\bin” y hacemos doble clic en el ejecutable mondongo.exe (Puede crear un acceso directo para no tener que repetir este proceso).

Ahora que ya tenemos el proyecto preparado y la base de datos preparada, vamos a conectar la base de datos y realizar las migraciones. Para ello los pasos a seguir son los siguientes:

- Paso 1: Acceder al archivo settings.py ubicado en pokedex/pokedex y modificar el apartado DATABASES. Nótese que el puerto indicado es el que viene por defecto en MongoDB, en caso de necesitar poner otro puerto para MongoDB, este también debe cambiar.

- Paso 2: En el terminal previamente creado, accedemos al directorio en el que se encuentra el archivo manage.py. (Puede usar el comando 
cd .\pokedex\)

- Paso 3: Debemos ejecutar estos dos comandos para crear las migraciones de la base de datos : 
    - python manage.py makemigrations
    - python manage.py migrate
- Paso 4: Ejecutamos el comando “python manage.py runserver” para lanzar el proyecto en local y accedemos a la url http://127.0.0.1:8000/.


