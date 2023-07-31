from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_blog'  # = mysql+pymysql://usuario:contraseña@ip/nombre_db

db = SQLAlchemy(app=app)
migrate = Migrate(app, db)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    clave = db.Column(db.String(100), nullable=False)
    

class Posteo(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.String(500), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    autor_id = db.Column(db.Integer, ForeignKey('usuario.id'), nullable=False)
    categoria_id = db.Column(db.Integer, ForeignKey('categoria.id'), nullable=False)

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500), nullable=False)
    fecha = db.Column(db.String(100), nullable=False)
    autor_id = db.Column(db.Integer, ForeignKey('usuario.id'), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)