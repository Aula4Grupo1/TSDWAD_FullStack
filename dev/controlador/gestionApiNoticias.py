# Modelar una clase que permita la comunicación con la base de datos en mysql
# para la tabla noticias

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
api = Api(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'noticias'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

class Noticias(Resource):

    def not_found(self):
        resp = jsonify('Noticia no encontrada')
        resp.status_code = 404
        return resp

    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM noticias")
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            _json = request.json
            _titulo = _json['titulo']
            _descripcion = _json['descripcion']
            _fecha = _json['fecha']
            _autor = _json['autor']
            _categoria = _json['categoria']
            _imagen = _json['imagen']
            _estado = _json['estado']
            # validate the received values
            if _titulo and _descripcion and _fecha and _autor and _categoria and _imagen and _estado and request.method == 'POST':
                # save edits
                sql = "INSERT INTO noticias(titulo, descripcion, fecha, autor, categoria, imagen, estado) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                data = (_titulo, _descripcion, _fecha, _autor, _categoria, _imagen, _estado,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('Noticia agregada exitosamente!')
                resp.status_code = 200
                return resp
            else:
                return not_found()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self):
        try:
            _json = request.json
            _id = _json['id']
            _titulo = _json['titulo']
            _descripcion = _json['descripcion']
            _fecha = _json['fecha']
            _autor = _json['autor']
            _categoria = _json['categoria']
            _imagen = _json['imagen']
            _estado = _json['estado']
            # validate the received values
            if _titulo and _descripcion and _fecha and _autor and _categoria and _imagen and _estado and _id and request.method == 'PUT':
                # save edits
                sql = "UPDATE noticias SET titulo=%s, descripcion=%s, fecha=%s, autor=%s, categoria=%s, imagen=%s, estado=%s WHERE id=%s"
                data = (_titulo, _descripcion, _fecha, _autor, _categoria, _imagen, _estado, _id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('Noticia actualizada exitosamente!')
                resp.status_code = 200
                return resp
            else:
                return not_found()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def delete(self):
        try:
            _json = request.json
            _id = _json['id']
            # validate the received values
            if _id and request.method == 'DELETE':
                # save edits
                sql = "DELETE FROM noticias WHERE id=%s"
                data = (_id,)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('Noticia eliminada exitosamente!')
                resp.status_code = 200
                return resp
            else:
                return not_found()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

# fin apiNoticias.py
# Path: dev\controlador\apiUsuarios.py
#    