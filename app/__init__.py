from flask import Flask

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave_secreta_para_sesiones'
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Importar rutas
    from app.rutas import registrar_rutas
    registrar_rutas(app)

    return app
