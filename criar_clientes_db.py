"""Cria o clientes.db (SQLite) com dados de exemplo, caso você ainda não tenha o seu."""
import sqlite3

con = sqlite3.connect("clientes.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        codigo INTEGER PRIMARY KEY,
        nome   TEXT NOT NULL,
        cidade TEXT
    )
""")

cur.executemany(
    "INSERT OR IGNORE INTO clientes (codigo, nome, cidade) VALUES (?, ?, ?)",
    [
        (1, "Maria Silva", "São Paulo"),
        (2, "João Souza", "Rio de Janeiro"),
        (3, "Ana Lima", "Belo Horizonte"),
    ],
)

con.commit()
con.close()
print("clientes.db criado.")
