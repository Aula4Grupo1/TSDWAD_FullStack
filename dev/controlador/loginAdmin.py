# Modelar el acceso del administrador a la pagina web.

# Crear formulario en html para el ingreso de datos de administrador.
import mysql.connector
from mysql.connector import errorcode
conexion1 = mysql.connector.connect(user='root', password='root', host='localhost', database='noticias')
cursor1 = conexion1.cursor()
#abrir tabla administrador
cursor1.execute("SELECT * FROM administrador")
#leer tabla administrador
rows = cursor1.fetchall()
print(rows)
#cerrar tabla administrador
cursor1.close()
conexion1.close()
# Cargar datos en tabla administrador
cursor1.execute("INSERT INTO administrador (nombre, apellido, usuario, clave, correo, estado) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, apellido, usuario, clave, correo, estado))
# Actualizar datos en tabla administrador
cursor1.execute("UPDATE administrador SET nombre = %s, apellido = %s, usuario = %s, clave = %s, correo = %s, estado = %s WHERE id = %s", (nombre, apellido, usuario, clave, correo, estado, id))
# Eliminar datos en tabla administrador
cursor1.execute("DELETE FROM administrador WHERE id = %s", (id,))