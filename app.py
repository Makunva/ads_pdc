from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def publicidad():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        # Aquí puedes procesar los datos (como guardar en base de datos o enviar un correo)
        print(f"Nombre: {nombre}, Correo: {correo}, Mensaje: {mensaje}")
    return render_template('publicidad.html')

if __name__ == '__main__':
    app.run(debug=True)
