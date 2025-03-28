@app.route('/', methods=['GET', 'POST'])
def publicidad():
    if request.method == 'POST':
        # Extraer datos del formulario
        nombre = request.form.get('nombre', '').strip()
        correo = request.form.get('correo', '').strip()
        mensaje = request.form.get('mensaje', '').strip()
        
        # Imprimir datos para depuración
        print(f"Nombre: {nombre}, Correo: {correo}, Mensaje: {mensaje}")
        
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
