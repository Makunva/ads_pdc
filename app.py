from flask import Flask, render_template, request, flash, redirect, url_for
import os

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Clave secreta para mensajes flash

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def publicidad():
    if request.method == 'POST':
        # Extraer datos del formulario
        nombre = request.form.get('nombre', '').strip()
        correo = request.form.get('correo', '').strip()
        mensaje = request.form.get('mensaje', '').strip()
        
        # Validación de datos
        if not nombre or not correo or not mensaje:
            flash("Por favor, completa todos los campos.")
        else:
            # Procesar datos (por ejemplo, guardar en base de datos o enviar correo)
            print(f"Nombre: {nombre}, Correo: {correo}, Mensaje: {mensaje}")
            flash("Mensaje enviado con éxito!")
            return redirect(url_for('publicidad'))
    
    return render_template('publicidad.html')

# Ejecución de la app
if __name__ == '__main__':
    # Debug habilitado para detectar errores rápidamente
    app.run(debug=True)
