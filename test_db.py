import mysql.connector

# Esta es la configuración que pide el libro
dbconfig = {
    'host': '127.0.0.1',
    'user': 'root', # Usaremos el usuario root por ahora
    'password': 'AkimiPichu26', # Tu contraseña secreta
    'database': 'vsearchlogdb',
}

try:
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT '¡Conexión Exitosa!'")
    result = cursor.fetchone()
    print(result[0])
    conn.close()
except Exception as e:
    print(f"Error: {e}")