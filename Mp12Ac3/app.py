from flask import Flask, render_template, request, redirect, url_for, session
from bd import obtenir_dades_terrasses, crear_terrassa, actualitzar_terrassa, eliminar_terrassa
from auth import autenticar_usuari
from bd import obtenir_usuaris, crear_usuari, actualitzar_usuari, eliminar_usuari

app = Flask(__name__)
app.secret_key = 'qualsevol_clau_segura'

@app.route('/')
def inici():
    if not session.get('usuari'):
        return redirect(url_for('login'))
    terrasses = obtenir_dades_terrasses()
    return render_template('index.html', terrasses=terrasses)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuari = request.form['username']
        contrasenya = request.form['contrasenya']
        if autenticar_usuari(usuari, contrasenya):
            session['usuari'] = usuari
            return redirect(url_for('inici'))
        else:
            return render_template('login.html', error="Credencials incorrectes.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/afegir', methods=['GET', 'POST'])
def afegir():
    if request.method == 'POST':
        crear_terrassa(
            request.form['emplacament'],
            request.form['taules'],
            request.form['cadires'],
            request.form['latitud'],
            request.form['longitud']
        )
        return redirect(url_for('inici'))
    return render_template('formulari.html', accio='Afegir', terrassa={})

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    from bd import obtenir_dades_terrasses
    terrasses = obtenir_dades_terrasses()
    terrassa = next((t for t in terrasses if t['id_terrassa'] == id), None)
    if request.method == 'POST':
        actualitzar_terrassa(
            id,
            request.form['emplacament'],
            request.form['taules'],
            request.form['cadires'],
            request.form['latitud'],
            request.form['longitud']
        )
        return redirect(url_for('inici'))
    return render_template('formulari.html', accio='Editar', terrassa=terrassa)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    eliminar_terrassa(id)
    return redirect(url_for('inici'))

@app.route('/inicial/usuari', methods=['GET', 'POST'])
def afegir_usuari_inicial():
    if request.method == 'POST':
        crear_usuari(request.form['username'], request.form['contrasenya'])
        return redirect(url_for('login'))
    return render_template('formulari_usuari.html', accio="Crear", usuari={})

@app.route('/usuaris')
def llistar_usuaris():
    if not session.get('usuari'):
        return redirect(url_for('login'))
    usuaris = obtenir_usuaris()
    return render_template('usuaris.html', usuaris=usuaris)

@app.route('/usuaris/afegir', methods=['GET', 'POST'])
def afegir_usuari():
    if request.method == 'POST':
        crear_usuari(request.form['username'], request.form['contrasenya'])
        return redirect(url_for('llistar_usuaris'))
    return render_template('formulari_usuari.html', accio="Afegir", usuari={})

@app.route('/usuaris/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuari(id):
    usuaris = obtenir_usuaris()
    usuari = next((u for u in usuaris if u['id_usuari'] == id), None)
    if request.method == 'POST':
        actualitzar_usuari(id, request.form['username'])
        return redirect(url_for('llistar_usuaris'))
    return render_template('formulari_usuari.html', accio="Editar", usuari=usuari)

@app.route('/usuaris/eliminar/<int:id>')
def eliminar_usuari_route(id):
    eliminar_usuari(id)
    return redirect(url_for('llistar_usuaris'))

if __name__ == '__main__':
    app.run(debug=True)
