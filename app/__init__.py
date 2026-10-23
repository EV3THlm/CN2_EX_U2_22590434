import os
from flask import Flask, render_template

from dotenv import load_dotenv

from app.extensions import db
from app.models import Contacto
from app.routes.contacto import contacto_bp

load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(contacto_bp, url_prefix='/contactos')

# Crear las tablas si no existen
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    # return 'Hola mundo'
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos)
