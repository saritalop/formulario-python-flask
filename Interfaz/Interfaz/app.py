from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__, static_folder='static')


# Configura la carpeta de carga
UPLOAD_FOLDER = 'archivos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def formulario():
    campos, datos = leer_datos('informacion.txt')
    num_columnas = len(campos) // 1 + len(campos) % 2  # Calcular el número de columnas
    return render_template('formulario.html', campos=campos, datos=datos, num_columnas=num_columnas)

@app.route('/guardar', methods=['POST'])
def guardar():
    # Leer los datos existentes del formulario
    datos_actuales = {}
    for campo in request.form:
        if campo != 'nuevo_campo' and campo != 'nuevo_valor' and campo != 'eliminar_campo':
            datos_actuales[campo] = request.form[campo]
            
    # Eliminar el campo si se envió como parte de la solicitud
    campo_a_eliminar = request.form.get('eliminar_campo')
    if campo_a_eliminar:
        # Eliminar el campo del diccionario de datos actuales
        datos_actuales.pop(campo_a_eliminar, None)
        
        # Eliminar el campo del archivo informacion.txt
        with open('informacion.txt', 'w') as file:
            for campo, valor in datos_actuales.items():
                file.write(f"{campo} = \"{valor}\"\n")
                
    # Obtener el nuevo campo y valor del formulario si se proporcionaron
    nuevo_campo = request.form.get('nuevo_campo', '').strip()
    nuevo_valor = request.form.get('nuevo_valor', '').strip()
    
    # Verificar si se proporcionaron valores para el nuevo campo y valor
    if nuevo_campo and nuevo_valor:
        # Actualizar los datos existentes con el nuevo campo y valor
        datos_actuales[nuevo_campo] = nuevo_valor
        
    # Escribir todos los datos en el nuevo archivo
    with open('informacion.txt', 'w') as file:
        for campo, valor in datos_actuales.items():
            file.write(f"{campo} = \"{valor}\"\n")
            
    # Procesar archivo adjunto si se proporcionó
    archivo_adjunto = request.files.get('archivo')
    if archivo_adjunto:
        # Guardar el archivo en la carpeta de carga sin cambiar el nombre
        archivo_adjunto.save(os.path.join(app.config['UPLOAD_FOLDER'], archivo_adjunto.filename))
        
    # Redirigir al formulario después de guardar
    return redirect(url_for('formulario'))

def leer_datos(archivo):
    campos = []
    datos = {}
    
    #Leer el archivo con el modo de lectura 'r'
    with open(archivo, 'r') as file:
        #Itera sobre cada linea de l archivo
        for line in file:
            key, value = line.strip().split('=')
            campos.append(key.strip())
            datos[key.strip()] = value.strip()
    return campos, datos

if __name__ == '__main__':
    
    if not os.path.exists(UPLOAD_FOLDER):
        #Se crea la carpeta en caso de que no exista
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True, port=5000)
