from app import app, db
from models import Usuario
from flask import render_template, redirect, url_for

@app.route('/add_user/<nombre>/<email>')
def add_user(nombre, email):
    usuario = Usuario(nombre=nombre, email=email)
    db.session.add(usuario)
    db.session.commit()
    return f'Usuario {nombre} agregado con éxito.'
    # return redirect(url_for('usuarios'))

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    return '<br>'.join([f'{u.id}. {u.nombre} - {u.email}' for u in usuarios])
    # return render_template('usuarios.html', usuarios=usuarios)