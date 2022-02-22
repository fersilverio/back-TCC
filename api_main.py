from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from rede_bayesiana import *
import os

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def func():
    string_entrada = request.get_json()
    prob_final = get_prediction(string_entrada)
    return jsonify({'probabilidade': prob_final})

@app.route('/teste')
@cross_origin()
def teste():
    return jsonify({'resp' : 'teste'})




if __name__ == '__main__':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port= port)