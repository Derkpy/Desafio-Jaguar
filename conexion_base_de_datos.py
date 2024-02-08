import mysql.connector

def creardatabase (nombredatabase):
    try:
        #conexion con el servidor
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Vengador23",
        )

        #creación del cursor
        cursor = conexion.cursor()

        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {nombredatabase};')
        resultado = "Se creó correctamente la base de datos."
        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()
        return resultado
    except:
        resultado = "Base de datos ya creada."
        return resultado

def creartablainfo():
    try:
        #conexion con el servidor
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Vengador23",
            database="proyecto"
        )

        #creación del cursor
        cursor = conexion.cursor()

        cursor.execute(f'CREATE TABLE IF NOT EXISTS preguntas' 
        "(id INT NOT NULL AUTO_INCREMENT,"
        "Pregunta VARCHAR (100) NOT NULL," 
        "Respuesta1 VARCHAR (100) NOT NULL,"
        "Respuesta2 VARCHAR (100) NOT NULL,"
        "Respuesta3 VARCHAR (100) NOT NULL,"
        "Respuesta4 VARCHAR (100) NOT NULL,"
        "Respuesta_Correcta VARCHAR (100) NOT NULL, "
        "PRIMARY KEY (id));")
        resultado = "Se creó correctamente la tabla."
        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()
        return resultado
    except:
        resultado = "Tabla ya creada."
        return resultado

def rellenartabla(cantidad):
    try:
        #conexion con el servidor
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Vengador23",
            database="proyecto"
        )
        for i in range(cantidad):
            #creación del cursor
            cursor = conexion.cursor()
            #informacion de insertado en la tabla  
            sql = "INSERT INTO preguntas (Pregunta, Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta_Correcta) VALUES (%s, %s, %s, %s, %s, %s)"
            val = ("Pregunta"+str(i+1),"A"+str(i+1) ,"B"+str(i+1) ,"C"+str(i+1) ,"D"+str(i+1), "RC"+str(i+1))
            cursor.execute(sql, val)
            conexion.commit()
        resultado = "Se relleno la tabla correctamente."
        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()
        return resultado
    except:
        resultado = "Ocurrió un error al intentar rellenar la tabla. Inténtelo de nuevo."
        return resultado 

def obtener_datos():
    try:
        #conexion con el servidor
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Vengador23",
            database="proyecto"
        )
        cursor = conexion.cursor()

        # Nombre de la tabla y columna que deseas obtener
        tabla = "preguntas"
        columna1 = "Pregunta"
        columna2 = "Respuesta1"
        columna3 = "Respuesta2"
        columna4 = "Respuesta3"
        columna5 = "Respuesta4"
        columna6 = "Respuesta_Correcta"

        # Consulta SQL para obtener los datos de la columna
        consulta = f"SELECT {columna1} FROM {tabla}"
        # Ejecutar la consulta
        cursor.execute(consulta)
        # Obtener todos los resultados en una lista
        preguntas = [fila[0] for fila in cursor.fetchall()]

        # Mismo proceso ya mencionado
        consulta = f"SELECT {columna2} FROM {tabla}"
        cursor.execute(consulta)
        respuesta1 = [fila[0] for fila in cursor.fetchall()]
        consulta = f"SELECT {columna3} FROM {tabla}"
        cursor.execute(consulta)
        respuesta2 = [fila[0] for fila in cursor.fetchall()]
        consulta = f"SELECT {columna4} FROM {tabla}"
        cursor.execute(consulta)
        respuesta3 = [fila[0] for fila in cursor.fetchall()]
        consulta = f"SELECT {columna5} FROM {tabla}"
        cursor.execute(consulta)
        respuesta4 = [fila[0] for fila in cursor.fetchall()]
        consulta = f"SELECT {columna6} FROM {tabla}"
        cursor.execute(consulta)
        respuesta_correcta = [fila[0] for fila in cursor.fetchall()]

        # Cerrar el cursor y la conexión a la base de datos
        cursor.close()
        conexion.close()

        preguntasA = []
        # Crear una lista para almacenar todas las listas
        # Iterar sobre los ciclos
        for i in range(len(preguntas)):
            # Crear una nueva lista en cada ciclo
            nueva_lista = []
            
            # Crear un diccionario en cada clave de la lista
            diccionario = {"p": preguntas[i], "r1": respuesta1[i], "r2": respuesta2[i],
                            "r3": respuesta3[i], "r4": respuesta4[i], "rc": respuesta_correcta[i]}
            
            nueva_lista.append(diccionario)

            # Agregar la nueva lista a la lista principal
            preguntasA.append(nueva_lista)

        # Imprimir la lista principal
        

        print("Busqueda terminada.")
        return preguntasA
    except:
        resultado = "Ocurrió un error al intentar buscar en la tabla. Inténtelo de nuevo."
        return resultado 
#crea una base de datos llamada proyecto

#print(creardatabase("proyecto"))

#crea la tabla de las preguntas

#print(creartablainfo())

#rellena la tabla con 10 datos, se puede aumentar la cantidad modificando el for de la funcion
#es mejor para cada prueba borrar la tabla para asi probar con solo la funcion o desactivarla para que no genere mas datos

#///////////////////////////////////////////////////
#print(rellenartabla(10))
#///////////////////////////////////////////////////

#obtiene la informacion contenida en la tabla

#obtener_datos()

