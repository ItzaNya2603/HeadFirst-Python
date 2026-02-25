import mysql.connector

class UseDatabase:
    # 1. ESTADO: El objeto "sabe"
    def __init__(self, config: dict) -> None:
        self.configuration = config

    # 2. Behavior AL ENTRAR: Abre la conexión y el cursor
    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    # 3. Behavior AL SALIR: Cierra todo automáticamente para evitar el consumo de recursos
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()