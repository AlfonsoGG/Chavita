from database import db


class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False, unique=True)
    amount = db.Column(db.String(70), nullable=False)

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount