from flask import Flask, render_template, request, flash, redirect, url_for
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Clave secreta para mensajes flash

# Configuración del correo electrónico
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
RECIPIENT_EMAIL = 'tu_correo_destino@example.com'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False

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
            
            # Enviar correo
            subject = "Nuevo mensaje de contacto"
            body = f"Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}"
            if send_email(subject, body):
                flash("Mensaje enviado con éxito y correo enviado.")
            else:
                flash("Mensaje enviado con éxito pero no se pudo enviar el correo.")
            
            return redirect(url_for('publicidad'))
    
    return render_template('publicidad.html')

# Ejecución de la app
if __name__ == '__main__':
    # Debug habilitado para detectar errores rápidamente
    app.run(debug=True)