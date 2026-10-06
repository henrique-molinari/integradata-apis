from flask import Flask, jsonify
import psycopg2
from config import NEON

app = Flask(__name__)

@app.route('/compras/<int:cliente>')
def compras(cliente):

    # Conexão com o PostgreSQL Neon (Connect to your branch)
    con = psycopg2.connect(**NEON)

    cur = con.cursor()

    cur.execute("""
        SELECT
            data_compra,
            valor
        FROM compras
        WHERE codigo_cliente = %s
    """, (cliente,))

    registros = cur.fetchall()

    con.close()

    resultado = []

    for item in registros:
        resultado.append({
            "data": item[0].strftime("%Y-%m-%d"),
            "valor": float(item[1])
        })

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
