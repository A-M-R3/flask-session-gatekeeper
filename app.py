from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_universidad_carlomagno'

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form.get('nombreInput')
        if nombre:
            session['nombre_usuario'] = nombre
            return redirect(url_for('bienvenida'))
    return render_template('index.html')

@app.route("/bienvenida")
def bienvenida():
    nombre = session.get('nombre_usuario')
    if not nombre:
        return redirect(url_for('home'))
    return render_template('index.html', bienvenida=True, nombre=nombre)

@app.route("/contenido")
def contenido():
    nombre = session.get('nombre_usuario')
    return render_template('contenido.html', nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)