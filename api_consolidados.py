from flask import Flask, jsonify
from pymongo import MongoClient
from config import MONGO_URI

app = Flask(__name__)

mongo = MongoClient(MONGO_URI)

db = mongo["integracao_dados"]

colecao = db["cliente_consolidado"]

@app.route('/consolidados')
def consolidados():

    lista = []

    for doc in colecao.find():

        doc["_id"] = str(doc["_id"])

        lista.append(doc)

    return jsonify(lista)

if __name__ == '__main__':
    app.run(port=5005, debug=True)
