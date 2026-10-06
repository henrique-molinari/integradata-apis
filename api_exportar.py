from flask import Flask, jsonify
from pymongo import MongoClient
from config import MONGO_URI
import pandas as pd
import os

app = Flask(__name__)

mongo = MongoClient(MONGO_URI)

db = mongo["integracao_dados"]

colecao = db["cliente_consolidado"]

@app.route('/exportar')
def exportar():

    registros = []

    for doc in colecao.find():

        registros.append({
            "codigo":
                doc["cliente"]["codigo"],

            "nome":
                doc["cliente"]["nome"],

            "cidade":
                doc["cliente"]["cidade"],

            "limite":
                doc["financeiro"]["limite"],

            "saldo":
                doc["financeiro"]["saldo"]
        })

    df = pd.DataFrame(registros)

    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "clientes_consolidados.xlsx"
    )

    df.to_excel(caminho, index=False)

    return jsonify({
        "arquivo":
        "clientes_consolidados.xlsx",
        "caminho":
        caminho,
        "registros":
        len(registros)
    })

if __name__ == '__main__':
    app.run(port=5006, debug=True)
