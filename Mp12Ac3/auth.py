import bcrypt
import mysql.connector

# Funció per encriptar contrasenya
def encriptar_contrasenya(contrasenya):
    return bcrypt.hashpw(contrasenya.encode('utf-8'), bcrypt.gensalt())

# Funció per verificar la contrasenya
def verificar_contrasenya(contrasenya, hash_contrasenya):
    if isinstance(hash_contrasenya, bytearray):
        hash_contrasenya = bytes(hash_contrasenya)
    return bcrypt.checkpw(contrasenya.encode('utf-8'), hash_contrasenya)


# Funció per autenticar usuaris
def autenticar_usuari(username, password):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='terrasses_db',
            user='root',
            password='Mo@petnapialS15'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT contrasenya FROM Usuaris WHERE username = %s", (username,))
        resultat = cursor.fetchone()
        conn.close()

        if resultat and verificar_contrasenya(password, resultat[0]):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error en l'autenticació: {e}")
        raise
