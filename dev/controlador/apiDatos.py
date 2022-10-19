# Modela una api para la gestion de datos de la tabla usuario y administrador
# 
# Definicion de los datos de la tabla usuario en mysql

import mysql.connector
from mysql.connector import errorcode
conexion1 = mysql.connector.connect(user='root', password='root', host='localhost', database='noticias')
cursor1 = conexion1.cursor()

# Definicion de los datos de la tabla administrador en mysql
# nombre de la tabla: administrador
# atributos: id, nombre, apellido, usuario, clave, correo, estado
# 
# Definicion de los datos de la tabla usuario en mysql
# nombre de la tabla: usuario
# atributos: id, nombre, apellido, usuario, clave, correo, estado
# 
# Definicion de los datos de la tabla noticias en mysql
# nombre de la tabla: noticias
# atributos: id, titulo, descripcion, fecha, autor, categoria, imagen, estado, url, apikey 
# 
# Definicion de los datos de la tabla categoria en mysql
# nombre de la tabla: categoria
# atributos: id, nombre, estado
# 
# Definicion de los datos de la tabla comentarios en mysql
# nombre de la tabla: comentarios
# atributos: id, id_noticia, nombre, correo, comentario, fecha, estado
# 
# Definicion de los datos de la tabla suscriptores en mysql
# nombre de la tabla: suscriptores
# atributos: id, nombre, correo, estado
# 




