import sqlite3

def connect():
    return sqlite3.connect("gastos.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        categoria TEXT,
        data TEXT DEFAULT CURRENT_DATE
    )
    """)
    conn.commit()
    conn.close()
