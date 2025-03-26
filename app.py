from flask import Flask, render_template, request  # Asegúrate de que Flask esté instalado correctamente

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def publicidad():
    if request.method == 'POST':
        # Extraer datos del formulario
        nombre = request.form.get('nombre', '')
        correo = request.form.get('correo', '')
        mensaje = request.form.get('mensaje', '')
        # Asegurarse de que no estén vacíos
        if not nombre or not correo or not mensaje:
            print("Datos incompletos en el formulario.")
        else:
            print(f"Nombre: {nombre}, Correo: {correo}, Mensaje: {mensaje}")
    return render_template('publicidad.html')

# Ejecución de la app
if __name__ == '__main__':
    # Debug habilitado para detectar errores rápidamente
    app.run(debug=True)
