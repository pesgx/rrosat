from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.modelos.conexion import obtener_conexion

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Ruta para la página de login
@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Página de inicio de sesión. Verifica el usuario y la contraseña.
    """
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Conexión a la base de datos
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_usuarios WHERE nombre_usuario = ? AND contrasena = ?", (usuario, contrasena))
        usuario_encontrado = cursor.fetchone()
        conexion.close()

        if usuario_encontrado:
            session['usuario'] = usuario  # Guardar usuario en sesión
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('pagina_principal'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

# Ruta para la página principal
@app.route('/principal')
def pagina_principal():
    """
    Página principal con botones para abrir las páginas CRUD de las tablas.
    """
    if 'usuario' not in session:
        flash('Debes iniciar sesión primero', 'warning')
        return redirect(url_for('login'))

    return render_template('principal.html')
