from flask import Flask
from database import db
from sqlalchemy_utils import create_database, database_exists
from routes.routes import blue_print
from flask_jwt_extended import JWTManager
import datetime
app = Flask(__name__)

#Base de datos

db_user = 'root'
db_pass = 'Strouts3313!'
db_host = 'localhost'
db_name = 'db_api_python'

DB_URL = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

app.config['JWT_SECRET_KEY']= '3st4-3s-M1-Cl4v3-S3cr3t4'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=12)

#JTW
jtw = JWTManager(app)

# Inicializamos SQLAlchemy
db.init_app(app)

#instacioamos las rutas
app.register_blueprint(blue_print)

# Creacion de la base de datos
with app.app_context():
    if not database_exists(DB_URL):
        create_database(DB_URL)
    db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)