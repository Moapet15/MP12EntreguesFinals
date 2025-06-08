import mysql.connector
from mysql.connector import Error
import logging
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega les variables d'entorn des del fitxer .env
# Ara la informació sensible es troba en un document .env que no es penja al repositori:
# DB_HOST=localhost
# DB_NAME=immobiliaria
# DB_USER=root
# DB_PASSWORD=la_teva_contrassenya
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
# print(DB_HOST,DB_NAME,DB_PASSWORD,DB_USER)

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Funció per connectar a la base de dades
def connectarBBDD():
    try:
        # Connexió a MySQL sense especificar base de dades
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD
        )
        
        cursor = conn.cursor()

        # Comprova si la base de dades existeix, i si no, la crea
        cursor.execute("CREATE DATABASE IF NOT EXISTS immobiliaria")

        # Ara connectem a la base de dades creada
        conn.database = DB_NAME

        return conn
    except mysql.connector.Error as e:
        print(f"Error de connexió a la base de dades: {e}")
        return None

# Inicialitzar la base de dades
def initBD(bd):
    if bd is None:
        print("La connexió a la base de dades ha fallat. No es pot inicialitzar la base de dades.")
        return
    
    cursor = bd.cursor()
    queries = [
        "CREATE TABLE IF NOT EXISTS usuaris ("
        "id INT PRIMARY KEY AUTO_INCREMENT,"
        "nom VARCHAR(50) NOT NULL,"
        "email VARCHAR(50) NOT NULL UNIQUE,"
        "password VARCHAR(50) NOT NULL,"
        "rebreOfertes TINYINT(1) DEFAULT 0,"
        "finquesPreferides TEXT,"
        "admin TINYINT(1) NOT NULL DEFAULT 0);",

        "CREATE TABLE IF NOT EXISTS immobles ("
        "id INT PRIMARY KEY AUTO_INCREMENT,"
        "referencia VARCHAR(50) NOT NULL,"
        "tipusFinca VARCHAR(50) NOT NULL,"
        "tipusHabitatge VARCHAR(50) NOT NULL,"
        "provincia VARCHAR(50) NOT NULL,"
        "municipi VARCHAR(50) NOT NULL,"
        "poblacio VARCHAR(50) NOT NULL,"
        "barri VARCHAR(50) NOT NULL,"
        "estatConservacio VARCHAR(50) NOT NULL,"
        "habitacions INT NOT NULL,"
        "superficieUtil INT NOT NULL,"
        "superficieConstruida INT NOT NULL,"
        "superficieTerreny INT NOT NULL,"
        "preu INT NOT NULL,"
        "pisos INT NOT NULL,"
        "descripcio TEXT,"
        "lavabos INT NOT NULL,"
        "terrassa TINYINT(1) NOT NULL DEFAULT 0,"
        "traster TINYINT(1) NOT NULL DEFAULT 0,"
        "garatge TINYINT(1) NOT NULL DEFAULT 0,"
        "jardi TINYINT(1) NOT NULL DEFAULT 0,"
        "qualificacioEnergetica INT NOT NULL,"
        "ruta_carpeta VARCHAR(255) NOT NULL,"
        "destacat TINYINT(1) NOT NULL DEFAULT 0);",

        "CREATE TABLE IF NOT EXISTS missatges ("
        "id INT PRIMARY KEY AUTO_INCREMENT,"
        "usuari_email VARCHAR(255) NOT NULL,"
        "finca_referencia VARCHAR(50),"
        "emissor ENUM('usuari', 'admin') NOT NULL,"
        "contingut TEXT NOT NULL,"
        "data_enviament DATETIME DEFAULT CURRENT_TIMESTAMP,"
        "llegit BOOLEAN DEFAULT FALSE,"
        "idAssociat INT DEFAULT NULL,"
        "FOREIGN KEY (usuari_email) REFERENCES usuaris(email) ON DELETE CASCADE,"
        "FOREIGN KEY (finca_referencia) REFERENCES immobles(referencia) ON DELETE SET NULL,"
        "FOREIGN KEY (idAssociat) REFERENCES missatges(id) ON DELETE CASCADE);",
        
        "CREATE TABLE IF NOT EXISTS consultes ("
        "id INT NOT NULL AUTO_INCREMENT,"
        "telefon VARCHAR(20) NOT NULL,"
        "email VARCHAR(100) NOT NULL,"
        "tipus VARCHAR(50) NOT NULL,"
        "missatge TEXT NOT NULL,"
        "data_creacio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
        "PRIMARY KEY (id);"
    ]

    for query in queries:
        cursor.execute(query)
    bd.commit()
    cursor.close()
    
# Funció per encaminar les peticions
def camiBD(solicitud, nom, email, password):
    # print(solicitud, nom, email, password)
    bd = connectarBBDD()
    if solicitud == "Login":
        return checkUser(bd, email, password)
    elif solicitud == "Signin":
        return crearUsuari(bd, nom, email, password)
    
# -------------------------------------------------- INICI DEL CRUD D'USUARIS --------------------------------------------------------------
    
# Crear un nou usuari
def crearUsuari(bd, nom, email, password):
    cursor = bd.cursor()
    try:
        query = "INSERT INTO usuaris (nom, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (nom, email, password))
        bd.commit()
        logging.info(f"Usuari creat: {nom} ({email})")  # Informem que l'usuari es va crear correctament
        return True
    except Exception as e:
        logging.error(f"Error en crear l'usuari {email}: {e}")  # Registre de l'error amb detall
        return False
    finally:
        cursor.close()
        
# Modificar informació de l'usuari
def modificarUsuari(bd, email, camps_a_modificar: dict): # AQUI REBREM UN DICCIONARI AMB LA INFORMACIÓ A MODIFICAR
    cursor = bd.cursor()
    print(camps_a_modificar)
    try:
        for camp, valor in camps_a_modificar.items():
            query = f"UPDATE usuaris SET {camp} = %s WHERE email = %s"
            cursor.execute(query, (valor, email))
        bd.commit()
        logging.info(f"Usuari amb email {email} modificat correctament.")  # Informem que l'usuari s'ha modificat
        return True
    except Exception as e:
        logging.error(f"Error en modificar l'usuari amb email {email}: {e}")  # Registre d'error detallat
        return False
    finally:
        cursor.close()
        
# Consultar la informació de l'usuari
def consultarUsuari(bd, usuari):
    cursor = bd.cursor()
    try:
        query = "SELECT nom, email, password, finquesPreferides FROM usuaris WHERE email=%s"
        cursor.execute(query, (usuari,))
        result = cursor.fetchone()
        if result:
            nom, email, password, finquesPreferides = result
            logging.info(f"Usuari amb email {email} trobat. Dades recuperades.")  # Informem que s'ha trobat l'usuari
            return {"nom": nom, "email": email, "password": password, "finquesPreferides": finquesPreferides}
        logging.warning(f"Usuari amb email {usuari} no trobat.")  # Avisem si l'usuari no existeix
        return None
    except Exception as e:
        logging.error(f"No hem pogut recuperar les dades de l'usuari {usuari}: {e}")  # Registre d'error
        return None
    finally:
        cursor.close()
        
# Borrar usuari
def borrarUsuari(bd, email):
    cursor = bd.cursor()
    try:
        query = "DELETE FROM usuaris WHERE email = %s"
        cursor.execute(query, (email,))
        bd.commit()
        logging.info(f"Usuari amb email {email} esborrat correctament.")  # Informem que l'usuari s'ha esborrat
        return True
    except Exception as e:
        logging.error(f"Error en borrar l'usuari amb email {email}: {e}")  # Registre d'error
        return False
    finally:
        cursor.close()

# -------------------------------------------------- FI DEL CRUD D'USUARIS ------------------------------------------------------------------

# -------------------------------------------------- INICI DEL CRUD D'IMMOBLES --------------------------------------------------------------

def inserirImmoble(bd, referencia, tipusFinca, tipusHabitatge, provincia, municipi, poblacio, barri, estat_conservacio,
                 habitacions, superficie_util, superficie_construida, superficie_terreny, preu, pisos,
                 lavabos, terrassa, traster, garatge, jardi, qualificacio_energetica, descripcio, filenames_str):
    print(referencia, tipusFinca, tipusHabitatge, provincia, municipi, poblacio, barri, estat_conservacio,
                 habitacions, superficie_util, superficie_construida, superficie_terreny, preu, pisos,
                 lavabos, terrassa, traster, garatge, jardi, qualificacio_energetica, descripcio, filenames_str)

    cursor = bd.cursor()
    try:
        query = """INSERT INTO immobles (
            referencia, tipusFinca, tipusHabitatge, provincia, municipi, poblacio, barri, 
            estatConservacio, habitacions, superficieUtil, superficieConstruida, 
            superficieTerreny, preu, pisos, lavabos, terrassa, 
            traster, garatge, jardi, qualificacioEnergetica, descripcio, ruta_carpeta
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s
        )"""
        cursor.execute(query, (referencia, tipusFinca, tipusHabitatge, provincia, municipi, poblacio, barri, estat_conservacio,
            habitacions, superficie_util, superficie_construida, superficie_terreny, preu, pisos,
            lavabos, terrassa, traster, garatge, jardi, qualificacio_energetica, descripcio, filenames_str))

        bd.commit()
        logging.info(f"Immoble amb referència {referencia} inserit correctament.")
        return True
    except Exception as e:
        logging.error(f"Error en inserir l'immoble amb referència {referencia}: {e}")
        return False
    finally:
        cursor.close()

def consultarImmobles(bd):
    cursor = bd.cursor()
    try:
        query = "SELECT * FROM immobles"
        cursor.execute(query)
        resultats = cursor.fetchall()
        immobles = []
        for fila in resultats:
            immoble = {
                'id': fila[0],
                'referencia': fila[1],  # Per exemple, columna 1 és 'referencia'
                'tipusHabitatge': fila[3],
                'provincia': fila[4],
                'municipi': fila[5],
                'poblacio': fila[6],
                'barri': fila[7],
                'superficieUtil': fila[10],
                'preu': fila[13],
                'habitacions': fila[4],
                'descripcio': fila[15],
                'qualificacioEnergetica': fila[21],
                'imatges': fila[22]
                # Afegir més camps segons la teva taula
            }
            immobles.append(immoble)
        logging.info("Consulta d'immobles realitzada correctament.")
        return immobles
    except Exception as e:
        logging.error(f"Error en consultar immobles: {e}")  # Error detallat
        return []
    finally:
        cursor.close()
        
def consultarImmoblesFiltrats(bd, filtres):
    cursor = bd.cursor()
    try:
        query = "SELECT * FROM immobles WHERE 1=1"
        valors = []

        if filtres.get("tipus"):
            query += " AND tipusHabitatge = %s"
            valors.append(filtres["tipus"])

        if filtres.get("preu_minim"):
            query += " AND preu >= %s"
            valors.append(filtres["preu_minim"])

        if filtres.get("preu_maxim"):
            query += " AND preu <= %s"
            valors.append(filtres["preu_maxim"])

        if filtres.get("poblacio"):
            query += " AND poblacio = %s"
            valors.append(filtres["poblacio"])

        if filtres.get("habitacions"):
            query += " AND habitacions = %s"
            valors.append(filtres["habitacions"])

        if filtres.get("banys"):
            query += " AND lavabos = %s"
            valors.append(filtres["banys"])

        if filtres.get("superficie_minima"):
            query += " AND superficieUtil >= %s"
            valors.append(filtres["superficie_minima"])

        if filtres.get("superficie_maxima"):
            query += " AND superficieUtil <= %s"
            valors.append(filtres["superficie_maxima"])
            
        if filtres.get("tipusFinca"):
            query += " AND tipusFinca = %s"
            valors.append(filtres["tipusFinca"])
            
        if filtres.get("id"):
            query += " AND id = %s"
            valors.append(filtres["id"])
            
        if filtres.get("referencia"):
            query += " AND referencia = %s"
            valors.append(filtres["referencia"])

        cursor.execute(query, valors)
        resultats = cursor.fetchall()

        # Processar resultats com abans
        immobles = []
        for fila in resultats:
            immoble = {
                'id': fila[0],
                'referencia': fila[1],  # Per exemple, columna 1 és 'referencia'
                'tipusHabitatge': fila[3],
                'provincia': fila[4],
                'municipi': fila[5],
                'poblacio': fila[6],
                'barri': fila[7],
                'superficieUtil': fila[10],
                'preu': fila[13],
                'habitacions': fila[4],
                'descripcio': fila[15],
                'qualificacioEnergetica': fila[21],
                'imatges': fila[22]
                # Afegir més camps segons la teva taula
            }
            immobles.append(immoble)

        return immobles

    except Exception as e:
        logging.error(f"Error en consultar immobles: {e}")
        return []
    finally:
        cursor.close()

def modificarImmoble(referencia, camp, nou_valor):
    bd = connectarBBDD()
    cursor = bd.cursor()

    sql = f"UPDATE immobles SET {camp} = %s WHERE referencia = %s"
    cursor.execute(sql, (nou_valor, referencia))

    bd.commit()
    cursor.close()
    bd.close()


def borrarImmoble(bd, referencia):
    cursor = bd.cursor()
    try:
        query = "DELETE FROM immobles WHERE referencia = %s"
        cursor.execute(query, (referencia,))
        bd.commit()
        logging.info(f"Immoble amb referència {referencia} esborrat correctament.")
        return True
    except Exception as e:
        logging.error(f"Error en esborrar l'immoble amb referència {referencia}: {e}")
        return False
    finally:
        cursor.close()
        
def mostrarDestacats(bd):
    cursor = bd.cursor()
    try:
        query = "SELECT * FROM immobles WHERE destacat = 1"
        cursor.execute(query)
        resultats = cursor.fetchall()
        
        immoblesDestacats = []
        for fila in resultats:
            immobleDestacat = {
                'id': fila[0],
                'referencia': fila[1],  # Per exemple, columna 1 és 'referencia'
                'tipusFinca': fila[2],
                'tipusHabitatge': fila[3],
                'provincia': fila[4],
                'municipi': fila[5],
                'poblacio': fila[6],
                'barri': fila[7],
                'superficieUtil': fila[10],
                'preu': fila[13],
                'habitacions': fila[4],
                'descripcio': fila[15],
                'qualificacioEnergetica': fila[21],
                'imatges': fila[22]
                # Afegir més camps segons la teva taula
            }
            
            immoblesDestacats.append(immobleDestacat)
            
        return immoblesDestacats
    except Exception as e:
        logging.error(f"Error en consultar immobles: {e}")
        return []
    finally:
        cursor.close()
        
        
# -------------------------------------------------- FI DEL CRUD D'IMMOBLES --------------------------------------------------------------

# Verificar si un usuari existeix
def checkUser(bd, email, password):
    cursor = bd.cursor()
    try:
        query = "SELECT id, nom, admin FROM usuaris WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        print(result)  # Mostrar el resultat per depurar

        if result:  # Si existeix l'usuari, retornem les dades
            user_id, nom, admin = result
            return {"id": user_id, "nom": nom, "admin": bool(admin)}  # Tornem un diccionari amb la informació

        return None  # Si no es troba l'usuari, retornem None

    except Exception as e:
        print(f"No s'ha pogut autenticar l'usuari: {e}")
        return None  # Retornem None en cas d'error

    finally:
        cursor.close()
        
def obtenirConversesIniciades(bd):
    cursor = bd.cursor()
    try:
        query = """
            SELECT m.id, m.usuari_email, m.finca_referencia, m.emissor, m.contingut, 
                   m.data_enviament, m.llegit,
                   i.tipusHabitatge, i.provincia, i.municipi
            FROM missatges m
            JOIN immobles i ON m.finca_referencia = i.referencia
            WHERE m.idAssociat IS NULL
            ORDER BY m.data_enviament DESC
        """
        cursor.execute(query)
        files = cursor.fetchall()

        converses = {}
        for fila in files:
            clau = (fila[1], fila[2])  # usuari_email + finca
            missatge = {
                "id": fila[0],
                "usuari_email": fila[1],
                "finca_referencia": fila[2],
                "emissor": fila[3],
                "contingut": fila[4],
                "data": fila[5],
                "llegit": fila[6]
            }
            finca_info = {
                "tipusHabitatge": fila[7],
                "provincia": fila[8],
                "municipi": fila[9]
            }
            if clau not in converses:
                converses[clau] = {
                    "usuari_email": fila[1],
                    "finca_referencia": fila[2],
                    "finca_info": finca_info,
                    "missatges": []
                }
            converses[clau]["missatges"].append(missatge)

        return list(converses.values())
    except Exception as e:
        print(f"Error obtenint converses iniciades: {e}")
        return []
    finally:
        cursor.close()

def obtenirConversesUsuari(bd, email):
    cursor = bd.cursor()
    try:
        query = """
            SELECT m.id, m.usuari_email, m.finca_referencia, m.emissor, m.contingut, m.data_enviament, m.llegit,
                   i.tipusHabitatge, i.provincia, i.municipi
            FROM missatges m
            JOIN immobles i ON m.finca_referencia = i.referencia
            WHERE m.usuari_email = %s
            ORDER BY m.finca_referencia, m.data_enviament
        """
        cursor.execute(query, (email,))
        files = cursor.fetchall()

        converses = {}
        for fila in files:
            clau = fila[2]  # finca_referencia com a clau
            missatge = {
                "id": fila[0],
                "usuari_email": fila[1],
                "finca_referencia": fila[2],
                "emissor": fila[3],
                "contingut": fila[4],
                "data": fila[5],
                "llegit": fila[6]
            }

            finca_info = {
                "tipusHabitatge": fila[7],
                "provincia": fila[8],
                "municipi": fila[9]
            }

            if clau not in converses:
                converses[clau] = {
                    "usuari_email": fila[1],
                    "finca_referencia": fila[2],
                    "finca_info": finca_info,
                    "missatges": []
                }

            converses[clau]["missatges"].append(missatge)

        return list(converses.values())
    except Exception as e:
        print(f"Error obtenint converses de l'usuari: {e}")
        return []
    finally:
        cursor.close()

def afegirMissatge(bd, usuari_email, finca_referencia, emissor, contingut, idAssociat=None):
    cursor = bd.cursor()
    try:
        if idAssociat:
            query = """
                INSERT INTO missatges (usuari_email, finca_referencia, emissor, contingut, idAssociat)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (usuari_email, finca_referencia, emissor, contingut, idAssociat))
        else:
            query = """
                INSERT INTO missatges (usuari_email, finca_referencia, emissor, contingut)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (usuari_email, finca_referencia, emissor, contingut))
        
        bd.commit()
        return True
    except Exception as e:
        print(f"Error afegint missatge: {e}")
        bd.rollback()
        return False
    finally:
        cursor.close()


def eliminarMissatgeUsuari(bd, missatge_id, usuari_email):
    cursor = bd.cursor()
    try:
        query = "DELETE FROM missatges WHERE id = %s AND usuari_email = %s"
        cursor.execute(query, (missatge_id, usuari_email))
        bd.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error esborrant missatge: {e}")
        bd.rollback()
        return False
    finally:
        cursor.close()

def obtenirConversaCompleta(bd, missatge_id):
    cursor = bd.cursor()
    try:
        # Primer recuperem la finca i usuari del missatge escollit
        cursor.execute("SELECT usuari_email, finca_referencia FROM missatges WHERE id = %s", (missatge_id,))
        fila = cursor.fetchone()
        if not fila:
            return None
        usuari_email, finca_referencia = fila

        # Ara recuperem tots els missatges d'aquesta conversa
        cursor.execute("""
            SELECT m.id, m.usuari_email, m.finca_referencia, m.emissor, m.contingut, m.data_enviament, m.llegit,
                   i.tipusHabitatge, i.provincia, i.municipi
            FROM missatges m
            JOIN immobles i ON m.finca_referencia = i.referencia
            WHERE m.usuari_email = %s AND m.finca_referencia = %s
            ORDER BY m.data_enviament
        """, (usuari_email, finca_referencia))

        files = cursor.fetchall()
        if not files:
            return None

        finca_info = {
            "tipusHabitatge": files[0][7],
            "provincia": files[0][8],
            "municipi": files[0][9]
        }

        missatges = []
        for fila in files:
            missatges.append({
                "id": fila[0],
                "usuari_email": fila[1],
                "finca_referencia": fila[2],
                "emissor": fila[3],
                "contingut": fila[4],
                "data": fila[5],
                "llegit": fila[6]
            })

        conversa = {
            "usuari_email": usuari_email,
            "finca_referencia": finca_referencia,
            "finca_info": finca_info,
            "missatges": missatges
        }

        return conversa
    except Exception as e:
        print(f"Error a obtenirConversaCompleta: {e}")
        return None
    finally:
        cursor.close()

def inserirConsulta(bd, telefon, email, tipus, missatge):
    cursor = bd.cursor()
    cursor.execute("""
        INSERT INTO consultes (telefon, email, tipus, missatge)
        VALUES (%s, %s, %s, %s)
    """, (telefon, email, tipus, missatge))
    bd.commit()


def obtenirConsultes(bd):
    cursor = bd.cursor()
    cursor.execute("SELECT id, telefon, email, tipus, missatge, data_creacio FROM consultes ORDER BY data_creacio DESC")
    consultes = cursor.fetchall()  # Retorna una llista de tuples amb totes les consultes
    return consultes
