from database import connect

def adicionar_gasto(descricao, valor, categoria):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO gastos (descricao, valor, categoria) VALUES (?, ?, ?)",
                   (descricao, valor, categoria))
    conn.commit()
    conn.close()

def listar_gastos():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gastos")
    lista = cursor.fetchall()
    conn.close()
    return lista

def total_gastos():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(valor) FROM gastos")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0
