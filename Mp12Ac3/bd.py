import mysql.connector
from mysql.connector import Error
import bcrypt

# Connexió a la base de dades
def connectar_bd():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='terrasses_db',
            user='root',
            password='Mo@petnapialS15'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error al connectar-se a la base de dades: {e}")
        raise

# Funció per obtenir dades de terrasses
def obtenir_dades_terrasses():
    try:
        conn = connectar_bd()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Terrasses")
        resultats = cursor.fetchall()
        conn.close()
        return resultats
    except Error as e:
        print(f"Error en obtenir les dades: {e}")
        raise

# Funció per crear una nova terrassa (POST)
def crear_terrassa(emplacament, taules, cadires, latitud, longitud):
    try:
        conn = connectar_bd()
        cursor = conn.cursor()
        query = """
        INSERT INTO Terrasses (emplacament, taules, cadires, latitud, longitud)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (emplacament, taules, cadires, latitud, longitud))
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error en crear la terrassa: {e}")
        raise

# Funció per actualitzar una terrassa existent (UPDATE)
def actualitzar_terrassa(id_terrassa, emplacament, taules, cadires, latitud, longitud):
    try:
        conn = connectar_bd()
        cursor = conn.cursor()
        query = """
        UPDATE Terrasses
        SET emplacament = %s, taules = %s, cadires = %s, latitud = %s, longitud = %s
        WHERE id_terrassa = %s
        """
        cursor.execute(query, (emplacament, taules, cadires, latitud, longitud, id_terrassa))
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error en actualitzar la terrassa: {e}")
        raise

# Funció per eliminar una terrassa (DELETE)
def eliminar_terrassa(id_terrassa):
    try:
        conn = connectar_bd()
        cursor = conn.cursor()
        query = "DELETE FROM Terrasses WHERE id_terrassa = %s"
        cursor.execute(query, (id_terrassa,))
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error en eliminar la terrassa: {e}")
        raise

# Funció per obtenir tots els usuaris
def obtenir_usuaris():
    try:
        conn = connectar_bd()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id_usuari, username FROM Usuaris")
        usuaris = cursor.fetchall()
        conn.close()
        return usuaris
    except Error as e:
        print(f"Error en obtenir usuaris: {e}")
        raise

# Crear usuari nou
def crear_usuari(username, contrasenya):
    try:
        hash_contrasenya = bcrypt.hashpw(contrasenya.encode('utf-8'), bcrypt.gensalt())
        conn = connectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuaris (username, contrasenya) VALUES (%s, %s)", (username, hash_contrasenya))
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error en crear usuari: {e}")
        raise

# Actualitzar usuari (només username, no contrasenya per simplicitat)
def actualitzar_usuari(id_usuari, username):
    try:
        conn = connectar_bd()
        cursor = conn.cursor()
        cursor.execute("UPDATE Usuaris SET username = %s WHERE id_usuari = %s", (username, id_usuari))
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error en actualitzar usuari: {e}")
        raise

# Eliminar usuari
def eliminar_usuari(id_usuari):
    try:
        conn = connectar_bd()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuaris WHERE id_usuari = %s", (id_usuari,))
        conn.commit()
        conn.close()
    except Error as e:
        print(f"Error en eliminar usuari: {e}")
        raise
