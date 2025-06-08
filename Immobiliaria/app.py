import json, os
from flask import Flask, flash, redirect, render_template, jsonify, session, request, url_for
from flask_session import Session  # ✅ Necessari per gestionar sessions
from bbdd import initBD, connectarBBDD, camiBD, consultarImmobles, inserirImmoble, borrarImmoble, modificarImmoble, consultarImmoblesFiltrats, mostrarDestacats, modificarUsuari, consultarUsuari, obtenirConversesUsuari, afegirMissatge, eliminarMissatgeUsuari, obtenirConversesIniciades, obtenirConversaCompleta, inserirConsulta, obtenirConsultes
from datetime import timedelta
from werkzeug.utils import secure_filename
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)
sessionSecretPassword = os.getenv("CONTRASSENYA_SESSIO")
LANGUAGES_PATH = "static/llenguatges/"
UPLOAD_FOLDER = "static/finques/"
WATCH_FOLDER = "finques/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['WATCH_FOLDER'] = WATCH_FOLDER


# Assegurar que la carpeta d'imatges existeix
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔹 Configurar Flask per utilitzar sessions
app.config["SECRET_KEY"] = sessionSecretPassword  # Clau per signar les cookies
app.config["SESSION_TYPE"] = "filesystem"  # Emmagatzemar la sessió en fitxers
app.config["SESSION_PERMANENT"] = True  # La sessió serà persistent
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=0, hours=0, minutes=30)  # Temps de vida de la sessió

Session(app)  # 🔹 Correcte: Inicialitza la sessió de Flask

# Carregar traduccions
def load_translations(lang_code):
    try:
        with open(f"{LANGUAGES_PATH}{lang_code}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"No s'ha trobat el fitxer de llenguatge: {lang_code}.json")
        return {}

def obtenir_idioma():
    # Agafa l'idioma de la sessió o 'ca' per defecte
    lang = session.get('lang', 'ca')
    # Si no és un dels idiomes suportats, torna anglès per defecte
    if lang not in ['ca', 'es', 'en']:
        lang = 'en'
    return lang

def obtenir_traduccions_actuals():
    lang = obtenir_idioma()
    return load_translations(lang)

@app.context_processor
def inject_translator():
    return dict(_=_)

@app.route('/set_lang', methods=['POST'])
def set_lang():
    data = request.get_json()
    if not data or 'lang' not in data:
        print(data)
        return jsonify(success=False, error="Falta l'idioma"), 400

    lang = data['lang']
    if lang not in ['ca', 'es', 'en']:
        lang = 'ca'

    session['lang'] = lang
    return jsonify(success=True)

@app.route('/canvia_idioma', methods=['POST'])
def canvia_idioma():
    data = request.get_json()
    idioma = data.get('idioma')
    if idioma in ['ca', 'es', 'en']:
        session['idioma'] = idioma
        return jsonify({'status': 'ok'})
    else:
        return jsonify({'error': 'Idioma no suportat'}), 400

@app.route("/", methods=["GET", "POST"])
def login():
    lang = request.args.get("lang")
    print(lang)
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    if request.method == "POST":
        # Obtenim les dades com a JSON
        # data = request.get_json()  # Els valors es passaran com a JSON des de JavaScript
        email = request.form.get("email")
        password = request.form.get("contrasenya")

        # Cridem a la funció camiBD per autenticar l'usuari
        user = camiBD("Login", "", email, password)
        filtres = {
        "tipus": request.args.get("tipus"),
        "preu_minim": request.args.get("preu_minim"),
        "preu_maxim": request.args.get("preu_maxim"),
        "poblacio": request.args.get("poblacio"),
        "habitacions": request.args.get("habitacions"),
        "banys": request.args.get("banys"),
        "superficie_minima": request.args.get("superficie_minima"),
        "superficie_maxima": request.args.get("superficie_maxima"),
        "tipusFinca": ""
    }

    try:
        bd = connectarBBDD()

        immoblesDestacats = mostrarDestacats(bd)
        # print(immoblesDestacats)
        
        if any(filtres.values()):
            immobles = consultarImmoblesFiltrats(bd, filtres)
        else:
            immobles = consultarImmobles(bd)

        return render_template(
            "subIndex.html", 
            translations=translations, 
            immobles=immobles, 
            immoblesDestacats=immoblesDestacats
        )
    except Exception as e:
        print("Error a home:", e)
        return render_template(
            "index.html", 
            translations=translations, 
            error="S'ha produït un error."
        )
    finally:
        try:
            bd.close()
        except:
            pass

    return render_template("index.html", translations=translations)

@app.route("/subIndex", methods=["GET"])
def subIndex():
    lang = request.args.get("lang")
    print(lang)
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte

    filtres = {
        "tipus": request.args.get("tipus"),
        "preu_minim": request.args.get("preu_minim"),
        "preu_maxim": request.args.get("preu_maxim"),
        "poblacio": request.args.get("poblacio"),
        "habitacions": request.args.get("habitacions"),
        "banys": request.args.get("banys"),
        "superficie_minima": request.args.get("superficie_minima"),
        "superficie_maxima": request.args.get("superficie_maxima"),
        "tipusFinca": ""
    }

    try:
        bd = connectarBBDD()

        immoblesDestacats = mostrarDestacats(bd)
        # print(immoblesDestacats)
        
        if any(filtres.values()):
            immobles = consultarImmoblesFiltrats(bd, filtres)
        else:
            immobles = consultarImmobles(bd)

        return render_template(
            "subIndex.html", 
            translations=translations, 
            immobles=immobles, 
            immoblesDestacats=immoblesDestacats
        )
    except Exception as e:
        print("Error a home:", e)
        return render_template(
            "subIndex.html", 
            translations=translations, 
            error="S'ha produït un error."
        )
    finally:
        try:
            bd.close()
        except:
            pass


@app.route("/aboutUs")
def aboutUs():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    return render_template("aboutUs.html", translations=translations)

@app.route("/serveis")
def serveis():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    return render_template("serveis.html", translations=translations)

@app.route("/finquesUrbanes")
def finquesUrbanes():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte

    # Recollim els filtres opcionals (només els que pot triar l'usuari)
    filtres = {
        "tipus": request.args.get("tipus"),
        "preu_minim": request.args.get("preu_minim"),
        "preu_maxim": request.args.get("preu_maxim"),
        "poblacio": request.args.get("poblacio"),
        "habitacions": request.args.get("habitacions"),
        "banys": request.args.get("banys"),
        "superficie_minima": request.args.get("superficie_minima"),
        "superficie_maxima": request.args.get("superficie_maxima"),
    }

    try:
        bd = connectarBBDD()

        # Comprovem si hi ha filtres actius (excloent els buits o None)
        filtres_actius = {k: v for k, v in filtres.items() if v}
        
        # Afegim sempre el filtre intern que només mostri les finques urbanes
        filtres_actius["tipusFinca"] = "Urbana"

        # Cridem la funció amb filtres si n’hi ha, sinó només amb "Urbana"
        immobles = consultarImmoblesFiltrats(bd, filtres_actius)

        return render_template("finquesUrbanes.html", translations=translations, immobles=immobles)

    except Exception as e:
        print("Error a home:", e)
        return render_template("finquesUrbanes.html", translations=translations, error="S'ha produït un error.")
    
    finally:
        try:
            bd.close()
        except:
            pass


@app.route("/finquesRustiques")
def finquesRustiques():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    
    # Recollim els filtres opcionals (només els que pot triar l'usuari)
    filtres = {
        "tipus": request.args.get("tipus"),
        "preu_minim": request.args.get("preu_minim"),
        "preu_maxim": request.args.get("preu_maxim"),
        "poblacio": request.args.get("poblacio"),
        "habitacions": request.args.get("habitacions"),
        "banys": request.args.get("banys"),
        "superficie_minima": request.args.get("superficie_minima"),
        "superficie_maxima": request.args.get("superficie_maxima"),
    }

    try:
        bd = connectarBBDD()

        # Comprovem si hi ha filtres actius (excloent els buits o None)
        filtres_actius = {k: v for k, v in filtres.items() if v}
        
        # Afegim sempre el filtre intern que només mostri les finques urbanes
        filtres_actius["tipusFinca"] = "Rustica"

        # Cridem la funció amb filtres si n’hi ha, sinó només amb "Urbana"
        immobles = consultarImmoblesFiltrats(bd, filtres_actius)
        
        return render_template("finquesRustiques.html", translations=translations, immobles=immobles)
    
    except Exception as e:
        print("Error a home:", e)
        return render_template("finquesRustiques.html", translations=translations, error="S'ha produït un error.")
    finally:
        try:
            bd.close()
        except:
            pass

@app.route("/lloguer")
def lloguer():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    
    # Recollim els filtres opcionals (només els que pot triar l'usuari)
    filtres = {
        "tipus": request.args.get("tipus"),
        "preu_minim": request.args.get("preu_minim"),
        "preu_maxim": request.args.get("preu_maxim"),
        "poblacio": request.args.get("poblacio"),
        "habitacions": request.args.get("habitacions"),
        "banys": request.args.get("banys"),
        "superficie_minima": request.args.get("superficie_minima"),
        "superficie_maxima": request.args.get("superficie_maxima"),
    }

    try:
        bd = connectarBBDD()

        # Comprovem si hi ha filtres actius (excloent els buits o None)
        filtres_actius = {k: v for k, v in filtres.items() if v}
        
        # Afegim sempre el filtre intern que només mostri les finques urbanes
        filtres_actius["tipusFinca"] = "Lloguer"

        # Cridem la funció amb filtres si n’hi ha, sinó només amb "Urbana"
        immobles = consultarImmoblesFiltrats(bd, filtres_actius)
        
        return render_template("lloguers.html", translations=translations, immobles=immobles)
    except Exception as e:
        print("Error a home:", e)
        return render_template("lloguers.html", translations=translations, error="S'ha produït un error.")
    finally:
        try:
            bd.close()
        except:
            pass

@app.route("/contacte")
def contacte():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    return render_template("contacte.html", translations=translations)

@app.route("/administrarUsuari")
def administrarUsuari():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte

    if "user" not in session:
        return redirect(url_for("subIndex"))
    bd = connectarBBDD()
    try:
        email = session["user"]["email"]

        # Obtenir l’usuari actualitzat de la base de dades
        usuari_db = consultarUsuari(bd, email)
        if not usuari_db:
            flash("No s'ha pogut carregar la informació de l'usuari", "error")
            return redirect(url_for("subIndex"))
        # Preparar preferits com a llista (si hi ha)
        preferits_str = usuari_db.get("finquesPreferides") or ""
        preferits_llista = [ref.strip() for ref in preferits_str.split(",") if ref.strip()]
        print("Referències preferides:", preferits_llista)

        finques = []
        for ref in preferits_llista:
            filtres = {"referencia": ref}
            resultats = consultarImmoblesFiltrats(bd, filtres)
            if resultats:
                finques.extend(resultats)
                print(resultats)

        # Converses sobre finques
        converses = obtenirConversesUsuari(bd, email)
        
        print(converses)

        return render_template(
        "administrarUsuari.html",
        usuari=usuari_db,
        preferits=preferits_llista,
        finques=finques,
        missatges=converses,  # canviat de converses a missatges
        translations=translations,
    )


    except Exception as e:
        print(f"Error carregant la pàgina d'usuari: {e}")
        return redirect(url_for("subIndex"))
    finally:
        bd.close()

@app.route("/administrarFinques", methods=["GET", "POST"])
def administrarFinques():
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    print(session)
    if "user" not in session:
        return redirect(url_for("subIndex"))

    try:
        user = session.get("user")
        if not user.get("admin", False):
            return redirect(url_for("subIndex"))

        bd = connectarBBDD()

        # Obtenir immobles
        immobles = consultarImmobles(bd)

        # Obtenir missatges (converses iniciades)
        missatges = obtenirConversesIniciades(bd)

        # 🔹 Obtenir consultes des de la base de dades
        consultes = obtenirConsultes(bd)

        return render_template(
            "administrarFinques.html",
            translations=translations,
            immobles=immobles,
            missatges=missatges,
            consultes=consultes,  # Afegim les consultes
            user=user
        )

    except Exception as e:
        print(f"Error en administrarFinques: {e}")
        return redirect(url_for("subIndex"))

    finally:
        try:
            bd.close()
        except:
            pass


@app.route("/signIn", methods=["POST"])
def signIn():
    if request.method == "POST":
        # Obtenim les dades com a JSON
        data = request.get_json()  # Els valors es passaran com a JSON des de JavaScript
        nom = data.get("nom")
        email = data.get("email")
        password = data.get("password")
        # print(nom, email, password)
        # Cridem a la funció camiBD per registrar l'usuari (suposant que fa la inserció a la BD)
        if camiBD("Signin", nom, email, password):
            # Respondre amb un missatge de JSON (significa que la inscripció va ser correcta)
            return jsonify({"success": True, "message": "S'ha registrat correctament"})
        else:
            return jsonify({"success": False, "message": "No ens hem pogut registrar"})

    # Si no és una petició POST, simplement mostrem la pàgina principal
    return render_template("subIndex.html")

@app.route("/logIn", methods=["POST"])
def logIn():
    if request.method == "POST":
        # Obtenim les dades com a JSON
        data = request.get_json()  # Els valors es passaran com a JSON des de JavaScript
        email = data.get("email")
        password = data.get("password")

        # Cridem a la funció camiBD per autenticar l'usuari
        user = camiBD("Login", "", email, password)

        if user:  # Si l'usuari és vàlid
            session["user"] = {"id": user["id"], "email": email, "admin": user["admin"]}
            print("Usuari loguejat:", session["user"])
            return jsonify({"success": True, "message": "Usuari autenticat correctament", "userData": session["user"]})

        return jsonify({"success": False, "message": "Email o contrasenya incorrectes"})

    return render_template("subIndex.html")

@app.route("/checkSession", methods=["GET"])
def check_session():
    """ Comprova si l'usuari està autenticat """
    user = session.get("user")
    if user:
        return jsonify({"authenticated": True, "user": user})
    return jsonify({"authenticated": False, "message": "No hi ha cap sessió activa"})

@app.route("/logout", methods=["POST"])
def logout():
    """ Tanca la sessió de l'usuari """
    session.pop("user", None)
    return jsonify({"success": True, "message": "Sessió tancada correctament"})

@app.route("/upload", methods=["POST"])
def upload():
    if "imatges" not in request.files or "referencia" not in request.form:
        return jsonify({"success": False, "message": "Dades incompletes."})

    referencia = request.form.get("referencia")
    tipusFinca = request.form.get("tipusFinca")
    tipusHabitatge = request.form.get("tipusHabitatge")
    provincia = request.form.get("provincia")
    municipi = request.form.get("municipi")
    poblacio = request.form.get("poblacio")
    barri = request.form.get("barri")
    estat_conservacio = request.form.get("estatConservacio")
    habitacions = int(request.form.get("habitacions"))
    superficie_util = int(request.form.get("superficieUtil"))
    superficie_construida = int(request.form.get("superficieConstruida"))
    superficie_terreny = int(request.form.get("superficieTerreny"))
    preu = int(request.form.get("preu"))
    pisos = int(request.form.get("pisos"))
    lavabos = int(request.form.get("lavabos"))
    qualificacio_energetica = int(request.form.get("qualificacioEnergetica"))
    descripcio = request.form.get("descripcio")
    
    terrassa = 1 if request.form.get("terrassa") == "on" else 0
    traster = 1 if request.form.get("traster") == "on" else 0
    garatge = 1 if request.form.get("garatge") == "on" else 0
    jardi = 1 if request.form.get("jardi") == "on" else 0

    files = request.files.getlist("imatges")

    print("TIPUS DE PREU:", type(habitacions))
    print("TIPUS DE PISO:", type(superficie_util))
    print("TIPUS DE LAVABOS:", type(superficie_construida))
    print("TIPUS DE SUPERFICIE TERRENY:", type(superficie_terreny))
    print("TIPUS DE PREU:", type(preu))
    print("TIPUS DE PISO:", type(pisos))
    print("TIPUS DE LAVABOS:", type(lavabos))
    print("TIPUS DE QUALIFICACIO ENERGETICA:", type(qualificacio_energetica))

    # Crear carpeta física on es guardaran les imatges
    carpeta_segura = secure_filename(f"Ref_{referencia}")
    ruta_fisica = os.path.join(app.config["UPLOAD_FOLDER"], carpeta_segura)
    ruta_virtual = os.path.join(app.config["WATCH_FOLDER"], carpeta_segura)
    os.makedirs(ruta_fisica, exist_ok=True)

    filenames = []
    for file in files:
        if file.filename:
            filename = secure_filename(file.filename)
            file_path = os.path.join(ruta_fisica, filename)
            file.save(file_path)

            # Ruta relativa per a guardar a la BD
            ruta_bd = os.path.join(ruta_virtual, filename).replace("\\", "/")

            filenames.append(ruta_bd)

    filenames_str = ", ".join(filenames)

    # print(f"Recuperem bé el tipus de finca? {tipusFinca}")
    
    bd = connectarBBDD()
    inserirImmoble(
        bd, referencia, tipusFinca, tipusHabitatge, provincia, municipi, poblacio, barri,
        estat_conservacio, habitacions, superficie_util, superficie_construida,
        superficie_terreny, preu, pisos, lavabos, terrassa, traster, garatge,
        jardi, qualificacio_energetica, descripcio, filenames_str
    )

    return jsonify({"success": True, "message": "Finca i imatges desades correctament!"})

@app.route('/delete', methods=['POST'])
def delete_immoble():
    referencia = request.form.get('referencia')
    bd = connectarBBDD()
    try:
        trobat = borrarImmoble(bd, referencia)  # Suposem que retorna True si s'ha esborrat, False si no trobat
        if trobat:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Immoble no trobat'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/modificar', methods=['POST'])
def guardarCanvi():
    dades = request.get_json()
    referencia = dades.get('referencia')
    camp = dades.get('camp')
    nou_valor = dades.get('nou_valor')

    if not (referencia and camp and nou_valor is not None):
        return jsonify(success=False, error="Falten camps requerits"), 400

    try:
        modificarImmoble(referencia, camp, nou_valor)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e)), 500
    
@app.route("/finca/<int:id>")
def finca(id):
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    bd = connectarBBDD()
    filtres = {"id": id}
    immoble = consultarImmoblesFiltrats(bd, filtres)
    bd.close()

    if immoble:
        return render_template("finca.html", immoble=immoble[0], translations=translations)
    else:
        return render_template("error.html", missatge="Immoble no trobat")

@app.route("/afegirPreferit", methods=["POST"])
def afegirPreferit():
    usuari = session.get("user")
    if not usuari:
        return jsonify({"status": "error", "missatge": "Usuari no autenticat"})

    referencia_immoble = request.form.get("referencia")
    if not referencia_immoble:
        return jsonify({"status": "error", "missatge": "Referència d'immoble no proporcionada"})

    bd = connectarBBDD()
    cursor = bd.cursor()

    try:
        email_usuari = usuari["email"]
        usuari_db = consultarUsuari(bd, email_usuari)

        preferits_actuals = usuari_db.get("finquesPreferides") or ""
        preferits_llista = [ref.strip() for ref in preferits_actuals.split(",") if ref.strip()]
        
        print(f"Llista retornada dels preferits: {preferits_llista}")

        if referencia_immoble not in preferits_llista:
            preferits_llista.append(referencia_immoble)
            preferits_nous = ", ".join(preferits_llista)
            
            print(f"Llista retornada dels preferits: {preferits_nous}")

            modificarUsuari(bd, email_usuari, {"finquesPreferides": preferits_nous})
            session["user"]["preferits"] = preferits_nous

        return jsonify({"status": "ok"})
    except Exception as e:
        print("Error afegint als preferits:", e)
        return jsonify({"status": "error", "missatge": str(e)})
    finally:
        cursor.close()
        bd.close()


@app.route("/eliminarPreferit", methods=["POST"])
def eliminarPreferit():
    usuari = session.get("user")
    if not usuari:
        return jsonify({"status": "error", "missatge": "Usuari no autenticat"})

    bd = connectarBBDD()
    cursor = bd.cursor()

    try:
        immoble = consultarImmobles(bd)
        referencia_immoble = immoble[0]["referencia"]
        usuari_id = usuari["id"]
        email_usuari = usuari["email"]

        print("id usuari:", usuari_id, "referencia immoble:", referencia_immoble)

        # Recuperem les dades actuals de la base de dades
        usuari_db = consultarUsuari(bd, email_usuari)
        preferits_actuals = usuari_db.get("finquesPreferides") or ""  # ← Prevenció si és None
        preferits_llista = [ref.strip() for ref in preferits_actuals.split(",") if ref.strip()]

        if referencia_immoble in preferits_llista:
            preferits_llista.remove(referencia_immoble)
            preferits_nous = ", ".join(preferits_llista)

            modificarUsuari(bd, email_usuari, {"finquesPreferides": preferits_nous})
            session["user"]["preferits"] = preferits_nous

        return jsonify({"status": "ok"})
    except Exception as e:
        print("Error eliminant preferit:", e)
        return jsonify({"status": "error", "missatge": str(e)})
    finally:
        cursor.close()
        bd.close()

@app.route("/afegirMissatge", methods=["POST"])
def afegir_missatge():
    if "user" not in session:
        return redirect(url_for("iniciSessio"))

    bd = connectarBBDD()
    try:
        usuari_email = request.form.get("usuari_email") or session["user"]["email"]
        finca_referencia = request.form.get("referencia")
        contingut = request.form.get("missatge") or request.form.get("missatge_resposta")
        idAssociat = request.form.get("idAssociat") or None

        # Determinem si qui envia el missatge és admin o usuari
        emissor = "admin" if session["user"].get("admin") else "usuari"

        if not finca_referencia or not contingut:
            flash("Falten dades per enviar el missatge.", "error")
            return redirect(request.referrer)

        resultat = afegirMissatge(bd, usuari_email, finca_referencia, emissor, contingut, idAssociat)
        if resultat:
            flash("Missatge enviat correctament.", "success")
        else:
            flash("No s'ha pogut enviar el missatge.", "error")

    except Exception as e:
        print(f"Error a la ruta afegirMissatge: {e}")
        flash("Error intern en enviar el missatge.", "error")
    finally:
        bd.close()

    return redirect(request.referrer)

@app.route("/eliminarMissatge", methods=["POST"])
def eliminar_missatge():
    if "user" not in session:
        return redirect(url_for("iniciSessio"))

    bd = connectarBBDD()
    try:
        missatge_id = request.form.get("missatge_id")
        usuari_email = session["user"]["email"]

        if not missatge_id:
            flash("Falta l'identificador del missatge.", "error")
            return redirect(request.referrer)

        resultat = eliminarMissatgeUsuari(bd, missatge_id, usuari_email)
        if resultat:
            flash("Missatge eliminat correctament.", "success")
        else:
            flash("No s'ha pogut eliminar el missatge.", "error")

    except Exception as e:
        print(f"Error a la ruta eliminarMissatge: {e}")
        flash("Error intern en eliminar el missatge.", "error")
    finally:
        bd.close()

    return redirect(request.referrer)

@app.route("/conversa/<int:missatge_id>")
def veure_conversa(missatge_id):
    lang = request.args.get("lang")
    if lang:
        session['lang'] = lang  # Actualitzem l'idioma a la sessió si es passa per URL

    translations = obtenir_traduccions_actuals()  # Usa l'idioma de la sessió o per defecte
    if "user" not in session:
        return redirect(url_for("iniciSessio"))

    lang = session.get('lang', 'ca')
    translations = load_translations(lang)

    bd = connectarBBDD()
    try:
        conversa = obtenirConversaCompleta(bd, missatge_id)
    except Exception as e:
        print(f"Error obtenint conversa completa: {e}")
        conversa = None
    finally:
        bd.close()

    if not conversa:
        flash("Conversa no trobada.", "error")
        return redirect(url_for("subIndex"))

    # Passa l'usuari de la sessió a la plantilla
    return render_template("conversaDetall.html", translations=translations, conversa=conversa, user=session.get("user"))

@app.route("/formulari_contacte", methods=["POST"])
def formulari_contacte():
    telefon = request.form.get("telefon")
    email = request.form.get("email")
    tipus = request.form.get("tipus")
    missatge = request.form.get("missatge")

    if not all([telefon, email, tipus, missatge]):
        flash("Tots els camps són obligatoris.", "error")
        return redirect(request.referrer or url_for("subIndex"))

    try:
        bd = connectarBBDD()
        inserirConsulta(bd, telefon, email, tipus, missatge)
        flash("Gràcies per contactar-nos! Et respondrem aviat.", "success")
    except Exception as e:
        print(f"Error guardant la consulta: {e}")
        flash("Hi ha hagut un error en enviar el formulari. Torna-ho a provar.", "error")
    finally:
        if bd:
            bd.close()

    return redirect(request.referrer or url_for("subIndex"))

app.config["TEMPLATES_AUTO_RELOAD"] = True

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
