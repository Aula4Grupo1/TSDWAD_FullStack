# Modelar el acceso del usuario a la pagina web.

# Crear formulario en html para el ingreso de datos de usuario.

from mysql.connector import errorcode
conexion1 = mysql.connector.connect(user='root', password='root', host='localhost', database='noticias')
cursor1 = conexion1.cursor()
# Cargar datos en tabla usuario
cursor1.execute("INSERT INTO usuario (nombre, apellido, usuario, clave, correo, estado) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, apellido, usuario, clave, correo, estado))
# Actualizar datos en tabla usuario
cursor1.execute("UPDATE usuario SET nombre = %s, apellido = %s, usuario = %s, clave = %s, correo = %s, estado = %s WHERE id = %s", (nombre, apellido, usuario, clave, correo, estado, id))
# Eliminar datos en tabla usuario
cursor1.execute("DELETE FROM usuario WHERE id = %s", (id,))


