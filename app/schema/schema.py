from flask_marshmallow import Marshmallow

ma = Marshmallow()

#Esquema de producto

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id','name','amount')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)