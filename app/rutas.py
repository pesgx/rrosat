from flask import render_template, request, redirect, url_for
from app.modelos.usuarios import verificar_usuario

def registrar_rutas(app):
    @app.route('/')
    def login():
        return render_template('login.html')

    @app.route('/menu')
    def menu_principal():
        return render_template('menu.html')

    # Rutas específicas por tabla
    @app.route('/clientes')
    def clientes():
        return render_template('clientes.html')
