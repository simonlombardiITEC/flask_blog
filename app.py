from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_blog'  # = mysql+pymysql://usuario:contraseña@ip/nombre_db

db = SQLAlchemy(app=app)
migrate = Migrate(app, db)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    clave = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.nombre
    

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.String(500), nullable=False)
    fecha_creacion = db.Column(db.Date, nullable=False)
    autor_id = db.Column(db.Integer, ForeignKey('usuario.id'), nullable=False)
    categoria_id = db.Column(db.Integer, ForeignKey('categoria.id'), nullable=False)

    def __str__(self):
        return self.nombre

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id = db.Column(db.Integer, primary_key=True)
    texto_comentario = db.Column(db.String(500), nullable=False)
    fecha_creacion = db.Column(db.String(100), nullable=False)
    autor_id = db.Column(db.Integer, ForeignKey('usuario.id'), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)


@app.route('/')
def index():
   return render_template(
       'index.html'
    )

@app.route('/inicio_sesion', methods=['POST'])
def iniciar_sesion():
    if request.method == 'POST':
        email_usuario = request.form['email']
        clave_usuario = request.form['clave']
        usuarios = db.session.query(Usuario).filter_by(correo = email_usuario,clave = clave_usuario).all()
        if usuarios== []:
            return (redirect(url_for('index')))
        else: 
            return render_template('inicio.html', usuario = usuarios)

@app.route('/registrarse', methods=['POST'])
def registrarse():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre']
        email_usuario = request.form['email']
        clave_usuario = request.form['clave']
        
        #Instancia
        nuevo_usuario = Usuario(nombre = nombre_usuario, correo = email_usuario, clave = clave_usuario)
        #Agregar Instancia
        db.session.add(nuevo_usuario)
        #Guardar Instancia 
        db.session.commit()
    return(redirect(url_for('index')))

@app.route('/inicio')
def inicio():    
    return render_template('inicio.html')

@app.route('/crear_post')
def crear_post():
    if request.method=='POST':
        usuario_id = request.form['usuario']
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        fecha = datetime.now()
        categoria_id = request.form['categoria']
        #Instancia
        nuevo_post = Post(titulo = titulo, contenido = contenido, fecha_cracion = fecha, autor_id = usuario_id, categoria_id = categoria_id)
        #Agregar Instancia
        db.session.add(nuevo_post)
        #Guardar Instancia
        db.session.commit()
        return render_template('inicio.html', usuario = db.session.query(Usuario).filter_by(id=usuario_id))
