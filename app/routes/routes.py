from flask import Blueprint, request, jsonify
from flask.globals import session
from models.models import Producto
from schema.schema import producto_schema,productos_schema
from database import db

blue_print = Blueprint('app', __name__)


# Ruta de inicio
@blue_print.route('/', methods=['GET'])
def inicio():
    return jsonify(respuesta='Api corriendo Exitosamente')

# Ruta - Crear producto
@blue_print.route('/api/productos', methods=['POST'])
def crear_producto():
    try:
        # obtener nombre de producto
        name = request.json.get('name')
        # obtener cantidad del producto
        amount = request.json.get('amount')
        # creamos nuevo producto

        existe_producto = Producto.query.filter_by(name=name).first()

        if existe_producto:
            return jsonify(respuesta='Producto ya existe'), 400

        nuevo_producto = Producto(name, amount)

        db.session.add(nuevo_producto)
        db.session.commit()

        return jsonify(respuesta='Producto almacenado Exitosamente'), 201

    except Exception:
        return jsonify(respuesta='Error en peticion'), 500


@blue_print.route('/api/producto', methods=['POST'])
def obtener_producto():
    try:
        # obtener producto
        nombre = request.json.get('name')
        print (nombre)
        producto = Producto.query(productos.name).filter(productos)
        print(producto)
        return jsonify(producto), 200
    except Exception:
        return jsonify(respuesta='Error en Peticion'), 500
